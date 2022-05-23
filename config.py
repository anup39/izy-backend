import logging
from os import getenv, path, makedirs
import hvac
import requests
from datetime import datetime, timedelta
import json


basedir = path.abspath(path.dirname(__file__))


def get_vault_token():
    user_name = getenv('USER_NAME')
    password = getenv('PASSWORD')
    url = getenv('VAULT_URL') + '/v1/auth/userpass/login/' + user_name
    res = requests.post(url, json={"password": password})
    if 'errors' in res.json():
        for message in res.json()['errors']:
            raise Exception('VaultError: ' + str(message))

    token = res.json()['auth']['client_token']
    return token


def get_vault_client(token):
    client = hvac.Client(
        url=getenv('VAULT_URL'),
        token=token)
    return client


def get_vault_module_params(client, mount_point, secret_path):
    return client.secrets.kv.v1.read_secret(
        path=secret_path,
        mount_point=mount_point,
    )


# --------- Module Token ---------
module_token = ""
module_token_expiry_time = None

# --------- Client -------------
token = get_vault_token()
client = get_vault_client(token)



class Config:
    DEBUG = False
    JWT_ALGORITHM = "RS256"
    JWT_DECODE_ALGORITHMS = "RS256"

    USER_NAME = getenv('USER_NAME')
    PASSWORD = getenv('PASSWORD')
    ENV = 'sandbox'

    MICRO_SERVICE_NAME = 'kiosk'
    CONFIGURATION_MOUNT_POINT = 'configuration'
    DATABASE_MOUNT_POINT = 'database'
    CONFIGURATION_PATH = f'{ENV}/parameters/{MICRO_SERVICE_NAME}'

    module_parameters = get_vault_module_params(
        client=client,
        secret_path=CONFIGURATION_PATH,
        mount_point=CONFIGURATION_MOUNT_POINT)['data']

    JWT_PUBLIC_KEY = get_vault_module_params(
        client=client,
        secret_path=module_parameters['jwt_public_path'],
        mount_point=CONFIGURATION_MOUNT_POINT)['data']['jwt_public_key']

    database_info = get_vault_module_params(
        client=client,
        secret_path=module_parameters['database_parameters_path'],
        mount_point=CONFIGURATION_MOUNT_POINT)['data']

    database_credentials = client.read(DATABASE_MOUNT_POINT + f'/creds/{MICRO_SERVICE_NAME}-{ENV}')

    db_credentials_expiry_time = datetime.now() + timedelta(seconds=database_credentials["lease_duration"])

    micro_service_urls = get_vault_module_params(
        client=client,
        secret_path=module_parameters['micro_service_urls_path'],
        mount_point=CONFIGURATION_MOUNT_POINT)['data']

    # --------- Swagger Parameters ---------
    SWAGGER_TITLE = module_parameters["swagger_title"]
    SWAGGER_DESCRIPTION = module_parameters["swagger_description"]
    SWAGGER_VERSION = module_parameters['swagger_version']

    # --------- Database Parameters ---------
    DB_DIALECT = database_info["database_dialect"]
    DB_HOST = database_info["database_host"]
    DB_PORT = database_info["database_port"]
    DB_USERNAME = database_credentials['data']["username"]
    DB_PASSWORD = database_credentials['data']["password"]
    DB_NAME = database_info["database_name"]


    print(DB_HOST,"db host")
    print(DB_PORT,"db port")
    print(DB_USERNAME,"username")
    print(DB_PASSWORD, "password")

    SQLALCHEMY_DATABASE_URI = f"{DB_DIALECT}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------- Micro Service URLs ---------
    URL_USERMANAGEMENT = micro_service_urls['usermanagement']
    URL_FILEHANDLER = micro_service_urls['filehandler']

    # --------- Logging ---------
    if not path.exists('./logs/'):
        makedirs('./logs/')
    if not path.exists('./logs/api.log'):
        open('./logs/api.log', 'x')

    logging.basicConfig(
        level=getenv("LOGLEVEL", "INFO"),
        handlers=[logging.FileHandler("./logs/api.log"), logging.StreamHandler()])

    if module_parameters['flask_logging'] == 'false':
        logging.disable(logging.WARNING)
        logging.disable(logging.ERROR)
        logging.disable(logging.INFO)
        logging.disable(logging.CRITICAL)

    TESTING = True if module_parameters['testing'] == 'true' else False