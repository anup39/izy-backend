from app.utils import input_validation_error, error_response, timestamp_format, get_new_entity_id, success, update_creator_access, data_access_error, paginate_query, forbidden_error
from sqlalchemy.exc import NoResultFound, IntegrityError
from app.authentication import get_token_user_id
from flask_sqlalchemy_session import current_session
from datetime import datetime
import requests
from .dto import OrganisationDto
api = OrganisationDto.api
logger = api.logger

from app.models.organisations import Organisations
from app.models.licensees import Licensees


def get_organisation_data(org_id):
    try:
        organisation = current_session.query(Organisations).filter(Organisations.organisation_id == org_id, Organisations.deleted_at == None).one()

        response_dict = {
            'organisation_number': organisation.organisation_number,
            'organisation_name': organisation.organisation_name,
            'address': organisation.address,
            'postal_code': organisation.postal_code,
            'city': organisation.city,
            'organisation_instances': {
                'licensees': [row.licensee_id for row in current_session.query(Licensees).filter(Licensees.organisation_id == org_id, Licensees.deleted_at == None).all()],
            },
            'created_at': timestamp_format(organisation.created_at),
            'updated_at': timestamp_format(organisation.updated_at)
        }

        return response_dict, 200

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Building ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()


def add_organisation(data):
    try:
        organisation_id = 'ORG-' + get_new_entity_id(Organisations)
        new_org = Organisations(
            organisation_id=organisation_id,
            organisation_number=data['organisation_number'],
            organisation_name=data['organisation_name'],
            address=data['address'],
            postal_code=data['postal_code'],
            city=data['city'],
            created_at=timestamp_format(datetime.now())
        )
        current_session.add(new_org)
        access_response = update_creator_access(user_id=get_token_user_id(), entity_id=organisation_id, role_id='ROL-1')
        if access_response.status_code != 200:
            return error_response('Could not update access for new entity, changes has not been committed')

        current_session.commit()

        return success(data={'organisation_id': organisation_id})

    except IntegrityError as e:
        logger.exception(e)
        return input_validation_error('Organisation with this organisation number already exists')

    except Exception as e:
        logger.exception(e)
        return error_response()


def get_organisation_registry_data(organisation_number):
    try:
        brreg_org_response = requests.get(url=f'https://data.brreg.no/enhetsregisteret/api/enheter/{organisation_number}')
        brreg_roles_response = requests.get(url=f'https://data.brreg.no/enhetsregisteret/api/enheter/{organisation_number}/roller')

        if brreg_org_response.status_code == 200:
            brreg_data = brreg_org_response.json()
            response_dict = {
                'organisation_number': brreg_data['organisasjonsnummer'],
                'organisation_name': brreg_data['navn'],
                'address': brreg_data['forretningsadresse']['adresse'],
                'postal_code': brreg_data['forretningsadresse']['postnummer'],
                'city': brreg_data['forretningsadresse']['poststed'],
                'representatives': []
            }

            if brreg_roles_response.status_code == 200:
                for role in brreg_roles_response.json()['rollegrupper'][0]['roller']:
                    role_dict = {
                        'first_name': role['person']['navn']['fornavn'],
                        'last_name': role['person']['navn']['etternavn'],
                        'date_of_birth': role['person']['fodselsdato'],
                        'role_code': role['type']['kode'],
                        'role_description': role['type']['beskrivelse'],
                        'resigned': role['fratraadt']
                    }
                    response_dict['representatives'].append(role_dict)

            return response_dict, 200

        else:
            error_response(f'Received error when calling BRREG, status code: [{brreg_org_response.status_code}]')

    except Exception as e:
        logger.exception(e)
        return error_response()


def update_organisation_data(data):
    try:
        organisation = current_session.query(Organisations).filter(Organisations.organisation_id == data['organisation_id'], Organisations.deleted_at == None).one()

        organisation.organisation_name = data['organisation_name']
        organisation.address = data['address']
        organisation.postal_code = data['postal_code']
        organisation.city = data['city']
        organisation.updated_at = timestamp_format(datetime.now())
        current_session.commit()

        return success(data={'organisation_id': data['organisation_id']})

    except NoResultFound as e:
        logger.exception(e)
        return error_response()
    except Exception as e:
        logger.exception(e)
        return error_response()


def soft_delete_organisation(organisation_id):
    try:
        licensees = [row[0] for row in current_session.query(Licensees).filter(Licensees.organisation_id == organisation_id, Licensees.deleted_at == None).with_entities(Licensees.licensee_id).all()]

        if len(licensees) != 0:
            return forbidden_error('Can not delete an organisation with active children entities',
                                   data={
                                       'licensees': licensees,
                                   })
        else:
            organisation = current_session.query(Organisations).filter(Organisations.organisation_id == organisation_id, Organisations.deleted_at == None).one()
            organisation.deleted_at = timestamp_format(datetime.now())
            current_session.commit()

            return success(data={'organisation_id': organisation_id})

    except NoResultFound as e:
        logger.exception(e)
        return error_response()
    except Exception as e:
        logger.exception(e)
        return error_response()


def get_organisation_licensees(organisation_id):
    try:
        licensees = current_session.query(Licensees).filter(Licensees.organisation_id == organisation_id, Licensees.deleted_at == None).all()
        response_list = []
        for licensee in licensees:
            licensee_dict = {
                'licensee_id': licensee.licensee_id,
                'licensee_name': licensee.licensee_name,
                'created_at': timestamp_format(licensee.created_at),
                'updated_at': timestamp_format(licensee.created_at)
            }
            response_list.append(licensee_dict)

        return response_list, 200

    except Exception as e:
        logger.exception(e)
        return error_response()
