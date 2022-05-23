from datetime import datetime
from flask_sqlalchemy import Pagination
from sqlalchemy.inspection import inspect
from flask_sqlalchemy_session import current_session
import requests
from flask_restx import reqparse
import config
from config import Config
from .support_classes import NoPagination
import os

def success(message="No message", data=None):
    if data:
        return {"status": 'Success', "reason": message, 'data': data}, 200
    else:
        return {"status": 'Success', "reason": message}, 200


def forbidden_error(reason="Unknown", data=None):
    return {'status': 'Forbidden Action Error', 'reason': reason, 'data': data}, 400


def data_access_error(reason="User does not have authorisation to access data this", code=401):
    return {'status': 'Data Access Error', 'reason': reason}, code


def input_validation_error(reason="Unknown", code=400):
    return {'status': 'Input Validation Failed', 'reason': reason}, code


def error_response(reason="Unknown", code=500):
    return {'status': 'Error', 'reason': reason}, code


def duplicate_error_response(reason="Unknown"):
    return {'status': 'Unique Violation Error', 'reason': reason}, 400


def timestamp_program(timestamp_string):
    if timestamp_string is None:
        return None
    else:
        return datetime.strptime(timestamp_string, '%Y-%m-%d %H:%M:%S.%f')


def timestamp_format(timestamp_object):
    if timestamp_object is None:
        return None
    else:
        return datetime.strftime(timestamp_object, '%Y-%m-%d %H:%M:%S.%f')


def get_new_entity_id(entity_class):
    id_column_name = inspect(entity_class).primary_key[0].name
    id_column = None
    for c in entity_class.__table__.columns:
        if str(c) == entity_class.__table__.name + '.' + id_column_name:
            id_column = c

    latest_entity_id = current_session.query(entity_class).order_by(entity_class.created_at.desc()).with_entities(id_column).first()
    if latest_entity_id is None:
        return str(0)
    else:
        return str(int(latest_entity_id[0].split('-')[1]) + 1)


def update_creator_access(user_id, entity_id, role_id):
    response = requests.put(
        Config.URL_USERMANAGEMENT + '/users/access/roles',
        json={
            'user_id': user_id,
            'entity_id': entity_id,
            'role_id': role_id
        },
        headers={'Authorization': 'Bearer ' + config.module_token}
    )
    return response


def upload_file(file_description, file):
    """
    :param file_description: Ex: building_cluster_header_image
    :param file: Takes in a b64 encoded string representation of a file
     """
    payload = {
        'file_description': file_description,
        'micro_service': Config.MICRO_SERVICE_NAME,
        'file_extension': 'file',
        'file': file
    }
    response = requests.post(
        url=Config.URL_FILEHANDLER + 'files/',
        json=payload,
        headers={'Authorization': 'Bearer ' + config.module_token}
    )
    return response


def get_file(file_id):
    response = requests.get(
        url=Config.URL_FILEHANDLER + 'files/',
        params={'file_id': file_id},
        headers={'Authorization': 'Bearer ' + config.module_token}
    )
    return response


def check_page_args(pg):
    if pg['paginate'] == 1:
        if not isinstance(pg['page'], int) or not isinstance(pg['limit'], int) or pg['page'] == 0 or pg['limit'] == 0:
            raise ValueError


def paginate_query(query, paginate, page, limit):
    # If pagination not active, return all results
    if paginate == 0:
        return NoPagination(query=query, items=query.all())

    # Query results
    items = query.limit(limit).offset((page - 1) * limit).all()

    # Calculate total
    if page == 1 and len(items) < limit:
        total = len(items)
    else:
        total = query.count()

    return Pagination(query, page, limit, total, items)


def token_args():
    tk_args = reqparse.RequestParser()
    tk_args.add_argument('Authorization', type=str, location='headers', help='Bearer Token', required=True)
    return tk_args

def pagination_args():
    pg_args = reqparse.RequestParser()
    pg_args.add_argument('paginate', type=int, required=True, help='Turn pagination on or off')
    pg_args.add_argument('page', type=int, required=False, help='Page number to fetch')
    pg_args.add_argument('limit', type=int, required=False, help='Page size')
    return pg_args

def date_filter_args():
    df_args = reqparse.RequestParser()
    df_args.add_argument('date_from', type=str, required=False, help='YYYY-MM-DD')
    df_args.add_argument('date_to', type=str, required=False, help='YYYY-MM-DD')
    return df_args

def order_by_args():
    ob_args = reqparse.RequestParser()
    ob_args.add_argument('order_by', type=str, required=False, help='Set field to order by')
    ob_args.add_argument('order_direction', type=str, required=False, help='Order direction: asc/desc')
    return ob_args

def search_string_args():
    ss_args = reqparse.RequestParser()
    ss_args.add_argument('search_string', type=str, required=False, help='Search text')
    return ss_args



    
