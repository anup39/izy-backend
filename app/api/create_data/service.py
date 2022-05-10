import requests
from flask_jwt_extended import create_access_token, decode_token
from jwt.exceptions import DecodeError
from app.utils import success, timestamp_format, input_validation_error, error_response
from sqlalchemy.exc import NoResultFound, IntegrityError
from flask_sqlalchemy_session import current_session
from datetime import datetime
from app import db
from .dto import CreateDataDto

from app.models.orders import Orders
from app.models.order_lines import OrderLines

logger = CreateDataDto.api.logger

from .data_dicts import create_dynamic_order

from .data_dicts import \
    organisation_insert, \
    building_insert, \
    licensee_insert, \
    building_graphic_profile_insert, \
    module_insert, \
    building_module_insert

model_data_list = [
    module_insert,
    organisation_insert,
    licensee_insert,
    building_insert,
    building_graphic_profile_insert,
    building_module_insert,
]


def create_stock_data():
    try:
        for model_type in model_data_list:
            for insert in model_type['inserts']:
                entry = model_type['class'](**insert)
                current_session.add(entry)
                current_session.commit()

        return success('Data created successfully')
    except Exception as e:
        logger.exception(e)
        return error_response()


def create_orders(num_orders):
    for i in range(num_orders):
        data = create_dynamic_order()
        order = data[0]
        new_order = Orders(**order)
        current_session.add(new_order)

        for order_line in data[1]:
            new_order_line = OrderLines(**order_line)
            current_session.add(new_order_line)

    current_session.commit()

    return success(f'{num_orders} orders created')