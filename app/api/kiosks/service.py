from app.utils import input_validation_error, error_response, timestamp_format, get_new_entity_id, success, update_creator_access, data_access_error, paginate_query, forbidden_error
from app.support_classes import QueryOrderBy, QueryDateFilter, QuerySearchFilter
from sqlalchemy.exc import NoResultFound, IntegrityError
from app.authentication import get_token_user_id
from flask_sqlalchemy_session import current_session
from sqlalchemy import asc, desc
from sqlalchemy import or_
from datetime import datetime
import requests
import json
from uuid import uuid4
from flask_jwt_extended import get_jwt

from .dto import KiosksDTO
api = KiosksDTO.api
logger = api.logger

from app.models.kiosks import Kiosks
from app.models.points_of_sales import PointsOfSales



def create_kiosks(data):
    try:
        kiosk_id = 'KIO-' + get_new_entity_id(Kiosks)

        new_kiosk = Kiosks(
            kiosk_id=kiosk_id,
            kiosk_name=data['kiosk_name'],
            description=data['description'],
            service_provider_id=data['service_provider_id'],
            building_module_id=data['building_module_id'],
            service_provider_internal_id=data['service_provider_internal_id'],
            header_image_id=data['header_image_id'],
            thumbnail_image_id=data['thumbnail_image_id'],
            # here get the building id and organization id from the service provider (left over part and i have some confusion here)
            # building_id = "testid",
            # organisation_id = "testorganizationid"
            created_at=timestamp_format(datetime.now())

        )

        # After the kiosk is created make a object in the points of sales tables
        points_of_sale_id = 'POS-' + get_new_entity_id(PointsOfSales)

        new_pos = PointsOfSales(
            pos_id = points_of_sale_id,
            pos_name = data['kiosk_name'],
            store_id = kiosk_id,
            created_at=timestamp_format(datetime.now())

        )

        current_session.add(new_kiosk)
        current_session.add(new_pos)
        current_session.commit()

        access_response = update_creator_access(user_id=get_token_user_id(), entity_id=kiosk_id, role_id='ROL-8')
        if access_response.status_code != 200:
            return error_response('Could not update access for new entity, changes has not been committed')

        current_session.commit()
        return success(data={'kiosk_id': kiosk_id})

    except Exception as e:
        logger.exception(e)
        return error_response()



