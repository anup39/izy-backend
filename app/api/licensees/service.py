from app.utils import success, timestamp_format, input_validation_error, error_response, get_new_entity_id, update_creator_access, forbidden_error
from sqlalchemy.exc import NoResultFound
from flask_sqlalchemy_session import current_session
from datetime import datetime
from app.authentication import get_token_user_id

from app.models.licensees import Licensees
from app.models.buildings import Buildings

from .dto import LicenseesDto
api = LicenseesDto.api
logger = api.logger

def get_licensee_data(licensee_id):
    try:
        licensee = current_session.query(Licensees).filter(Licensees.licensee_id == licensee_id, Licensees.deleted_at == None).one()
        buildings = [{'building_id': row.building_id, 'building_name': row.building_name} for row in current_session.query(Buildings).filter(Buildings.licensee_id == licensee_id, Buildings.deleted_at == None).all()]
        response_dict = {
            'licensee_id': licensee.licensee_id,
            'licensee_name': licensee.licensee_name,
            'organisation_id': licensee.organisation_id,
            'buildings': buildings,
            'created_at': timestamp_format(licensee.created_at),
            'updated_at': timestamp_format(licensee.updated_at)
        }

        return response_dict, 200

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Licensee ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()


def create_licensee(data):
    try:
        licensee_id = 'LIC-' + get_new_entity_id(Licensees)
        new_lic = Licensees(
            licensee_id=licensee_id,
            licensee_name=data['licensee_name'],
            organisation_id=data['organisation_id'],
            created_at=timestamp_format(datetime.now())
        )
        current_session.add(new_lic)
        current_session.commit()

        access_response = update_creator_access(user_id=get_token_user_id(), entity_id=licensee_id, role_id='ROL-3')
        if access_response.status_code != 200:
            return error_response('Could not update access for new entity, changes has not been committed')

        current_session.commit()
        return success(data={'licensee_id': licensee_id})

    except Exception as e:
        logger.exception(e)
        return error_response()


def update_licensee_base_data(data):
    try:
        licensee = current_session.query(Licensees).filter(Licensees.licensee_id == data['licensee_id'], Licensees.deleted_at == None).one()
        licensee.licensee_name = data['licensee_name']
        licensee.updated_at = timestamp_format(datetime.now())

        current_session.commit()

        return success(data={'licensee_id': licensee.licensee_id, 'licensee_name': data['licensee_name']})

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Licensee ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()


def soft_delete_licensee(licensee_id):
    try:
        buildings = [row.building_id for row in current_session.query(Buildings).filter(Buildings.licensee_id == licensee_id, Buildings.deleted_at == None).all()]

        if len(buildings) != 0:
            return forbidden_error('Can not delete an organisation with active children entities',
                                   data={
                                       'buildings': buildings,
                                   })

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Licensee ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()


def get_licensee_buildings(licensee_id):
    try:
        response_list = []
        buildings = current_session.query(Buildings).filter(Buildings.licensee_id == licensee_id, Licensees.deleted_at == None).all()
        for building in buildings:
            building_dict = {
                'building_id': building.building_id,
                'building_name': building.building_name,
                'created_at': timestamp_format(building.created_at),
                'updated_at': timestamp_format(building.updated_at)
            }
            response_list.append(building_dict)

        return response_list, 200

    except Exception as e:
        logger.exception(e)
        return error_response()