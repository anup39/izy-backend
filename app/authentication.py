from functools import wraps
import logging
from flask import request, abort, g
import jwt
from jwt.exceptions import DecodeError
from app.utils import error_response
from app.support_classes import AuthenticationError
from flask_jwt_extended import get_jwt
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError
from flask import globals
import json
import os

logger = logging.getLogger('api')


def check_entity_access(endpoint_id, entity_id):
    token = get_jwt()
    if 'admin_access' in token:
        if os.getenv('MICRO_SERVICE_NAME') in token['admin_access']:
            return 0
    if entity_id in token['entity_access']:
        if endpoint_id not in token['entity_access'][entity_id]:
            raise AuthenticationError(logger='api', msg=f'user_id: {token["user_id"]}, user_email: {token["email"]}, endpoint_id: {endpoint_id}, entity_id: {entity_id}')
        else:
            return 0
    else:
        raise AuthenticationError(logger='api', msg=f'user_id: {token["user_id"]}, user_email: {token["email"]}, endpoint_id: {endpoint_id}, entity_id: {entity_id}')



def get_token_user_id():
    try:

        return get_jwt()['user_id']

    except Exception as e:
        logger.exception(e)
        return error_response()
