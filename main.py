import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy_session import flask_scoped_session
from dotenv import load_dotenv
import config
from config import Config
from datetime import datetime, timedelta
import click
from flask_migrate import Migrate
from app import create_app, db
from flask_sqlalchemy_session import current_session
from flask_jwt_extended import decode_token
import requests


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app()
migrate = Migrate(app, db)


@app.before_first_request
def init_params():
    # Init flask db connection
    flask_scoped_session(sessionmaker(
        bind=create_engine(
            f"{Config.DB_DIALECT}://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}",
            pool_size=5),
        autocommit=False,
        autoflush=False),
        app)

    # Init module token from USM module login
    resp = requests.post(
        url=Config.URL_USERMANAGEMENT + '/users/module-login',
        json={'username': os.getenv('USER_NAME'), 'password': os.getenv('PASSWORD')})
    if resp.status_code != 200:
        raise Exception('Error when getting module token from USM: ' + str(resp.status_code) + ' ' + resp.reason)
    config.module_token = resp.json()

    config.module_token_expiry_time = datetime.now() + timedelta(seconds=decode_token(config.module_token)['exp'])


@app.before_request
def update_params(quit_counter=0):
    # Update DB params
    if Config.db_credentials_expiry_time < datetime.now():
        try:
            info = config.client.read(Config.DATABASE_MOUNT_POINT + f'/creds/{Config.MICRO_SERVICE_NAME}-{Config.ENV}')
            data = info['data']
            Config.db_credentials_expiry_time = datetime.now() + timedelta(seconds=info['lease_duration'])
            Config.DB_USERNAME = data['username']
            Config.DB_PASSWORD = data['password']
            current_session.close()
            flask_scoped_session(sessionmaker(
                bind=create_engine(
                    f"{Config.DB_DIALECT}://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}",
                    pool_size=5),
                autocommit=False,
                autoflush=False),
                app)
        except:
            # If client.read fails, update vault_token and try again immediately
            config.client = config.get_vault_client(config.get_vault_token())
            # If client.read fails multiple times, update vault_token and try again after X seconds
            if quit_counter > 0:
                time.sleep(5)
            # If client.read has failed X times, quit run
            if quit_counter > 2:
                raise Exception

            # Nested call to try again
            update_params(quit_counter=quit_counter + 1)

    # Update module token params
    if config.module_token_expiry_time < datetime.now():
        config.module_token = requests.post(Config.URL_USERMANAGEMENT + '/users/module-login', json={'username': os.getenv('USER_NAME'), 'password': os.getenv('PASSWORD')}).json()
        config.token_expiry_time = datetime.now() + timedelta(seconds=decode_token(config.module_token)['exp'])


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.cli.command()
@click.argument("test_names", nargs=-1)
def test(test_names):
    """ Run unit tests """
    import unittest

    if test_names:
        """ Run specific unit tests.

        Example:
        $ flask test tests.test_auth_api tests.test_user_model ...
        """
        tests = unittest.TestLoader().loadTestsFromNames(test_names)

    else:
        tests = unittest.TestLoader().discover("tests", pattern="test*.py")

    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0

    # Return 1 if tests failed, won't reach here if succeeded.
    return 1
