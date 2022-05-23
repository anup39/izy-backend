from app.utils import input_validation_error, error_response, timestamp_format, get_new_entity_id, success, update_creator_access, data_access_error, paginate_query, upload_file
from ...support_classes import AuthenticationError, QueryOrderBy
from sqlalchemy.exc import NoResultFound, IntegrityError
from flask_sqlalchemy_session import current_session
from app.models.building_graphic_profiles import BuildingGraphicProfiles
from app.models.buildings import Buildings
from app.models.building_modules import BuildingModules
from app.models.modules import Modules
from datetime import datetime
from random import randint
from app.authentication import get_token_user_id, check_entity_access
from .dto import BuildingsDTO


api = BuildingsDTO.api
logger = api.logger


def get_building_data(building_id):
    try:
        # Get data
        building_data = current_session.query(Buildings).filter(Buildings.building_id == building_id, Buildings.deleted_at == None).one()
        modules = {row.module_id: row.module_name for row in current_session.query(Modules).all()}
        building_modules = current_session.query(BuildingModules).filter(BuildingModules.building_id == building_id).all()
        building_graphic_profile = current_session.query(BuildingGraphicProfiles).filter(BuildingGraphicProfiles.building_id == building_id).one()

        # Get building modules in building
        building_modules_list = []
        for building_module in building_modules:
            building_module_dict = {
                'building_module_id': building_module.building_module_id,
                'module_id': building_module.module_id,
                'module_name': modules[building_module.module_id],
            }
            building_modules_list.append(building_module_dict)

        response_dict = {
            'building_id': building_data.building_id,
            'building_name': building_data.building_name,
            'licensee_id': building_data.licensee_id,
            'postal_address': {
                'country': building_data.country,
                'country_code': building_data.country_code,
                'postal_number': building_data.postal_number,
                'address': building_data.address,
                'city': building_data.city
            },
            'building_modules': building_modules_list,
            'graphic_profile': {
                'primary_color_hex': building_graphic_profile.primary_color_hex,
                'accent_color_hex': building_graphic_profile.accent_color_hex,
                'background_color_hex': building_graphic_profile.background_color_hex,
                'header_image_id': str(building_graphic_profile.header_image_id)
            },
            'latitude': building_data.latitude,
            'longitude': building_data.longitude,
            'square_meters': building_data.square_meters,
            'number_of_users': building_data.number_of_users,
            'number_of_floors': building_data.number_of_floors,
            'user_app_self_registration': building_data.user_app_self_registration,
            'private_building': building_data.private_building,
            'created_at': timestamp_format(building_data.created_at),
            'updated_at': timestamp_format(building_data.updated_at),
            'deleted_at': timestamp_format(building_data.deleted_at),
        }


        return response_dict, 200

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Building ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()

def create_building(data):
    try:
        building_id = 'BUI-' + get_new_entity_id(Buildings)
        tenant_registration_codes = [row.tenant_registration_code for row in current_session.query(Buildings).with_entities(Buildings.tenant_registration_code).all()]
        tenant_registration_code = randint(10000, 99999)
        while tenant_registration_code in tenant_registration_codes:
            tenant_registration_code = randint(10000, 99999) 

        new_building = Buildings(
            building_id=building_id,
            building_name=data['building_name'],
            licensee_id=data['licensee_id'],
            user_app_self_registration=data['user_app_self_registration'],
            tenant_registration_code=tenant_registration_code,
            private_building=data['private_building'],
            country=data['postal_address']['country'],
            country_code=data['postal_address']['country_code'],
            postal_number=data['postal_address']['postal_number'],
            address=data['postal_address']['address'],
            city=data['postal_address']['city'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            square_meters=data['square_meters'],
            number_of_users=data['number_of_users'],
            number_of_floors=data['number_of_floors'],
            created_at=timestamp_format(datetime.now())
        )
        current_session.add(new_building)
        current_session.commit()

        if data['graphic_profile']['header_image']:
            header_image_id = upload_file(file_description='building_header_image', file=data['graphic_profile']['header_image'])
        else:
            header_image_id = None

        new_graphic_profile = BuildingGraphicProfiles(
            building_id=building_id,
            primary_color_hex=data['graphic_profile']['primary_color_hex'],
            accent_color_hex=data['graphic_profile']['accent_color_hex'],
            background_color_hex=data['graphic_profile']['background_color_hex'],
            header_image_id=header_image_id
        )
        current_session.add(new_graphic_profile)


        for module in current_session.query(Modules).all():
            new_building_module = BuildingModules(
                module_id=module.module_id,
                building_id=building_id,
                active=0
            )
            current_session.add(new_building_module)


        access_response = update_creator_access(user_id=get_token_user_id(), entity_id=building_id, role_id='ROL-8')
        if access_response.status_code != 200:
            return error_response('Could not update access for new entity, changes has not been committed')

        current_session.commit()
        return success(data={'building_id': building_id})

    except Exception as e:
        logger.exception(e)
        return error_response()

def update_building_base_data(data):
    try:
        building = current_session.query(Buildings).filter(Buildings.building_id == data['building_id'], Buildings.deleted_at == None).one()
        building.building_name = data['building_name']
        building.user_app_self_registration = data['user_app_self_registration']
        building.private_building = data['private_building']
        building.country = data['postal_address']['country']
        building.country_code = data['postal_address']['country_code']
        building.postal_number = data['postal_address']['postal_number']
        building.address = data['postal_address']['address']
        building.city = data['postal_address']['city']
        building.latitude = data['latitude']
        building.longitude = data['longitude']
        building.square_meters = data['square_meters']
        building.number_of_users = data['number_of_users']
        building.number_of_floors = data['number_of_floors']
        building.updated_at = timestamp_format(datetime.now())
        current_session.commit()

        return success()

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Building ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()


def soft_delete_building(building_id):
    try:
        building = current_session.query(Buildings).filter(Buildings.building_id == building_id, Buildings.deleted_at == None).one()
        building.deleted_at = datetime.now()
        current_session.commit()

        return success('Building deleted')

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Building ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()


def get_building_modules(building_id):
    try:
        modules = {row.module_id: row.module_name for row in current_session.query(Modules).all()}
        building_modules = current_session.query(BuildingModules).filter(BuildingModules.building_id == building_id).all()
        building_module_list = []
        for building_module in building_modules:
            building_module_dict = {
                'building_module_id': building_module.building_module_id,
                'module_id': building_module.module_id,
                'module_name': modules[building_module.module_id],
                'active': building_module.active
            }
            building_module_list.append(building_module_dict)

        return building_module_list, 200

    except Exception as e:
        logger.exception(e)
        return error_response()

        


def update_building_module_state(data, endpoint_id):
    try:
        building_module = current_session.query(BuildingModules).filter(BuildingModules.building_module_id == data['building_module_id']).one()
        check_entity_access(endpoint_id=endpoint_id, entity_id=building_module.building_id)
        building_module.active = data['active']
        current_session.flush()
        current_session.commit()

        return success(data={'building_module_id': building_module.building_module_id, 'active': building_module.active})

    except AuthenticationError as e:
        logger.exception(e)
        return data_access_error()
    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Building module ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()


def get_all_public_buildings(pg_args, ob_args):
    try:
        ob = QueryOrderBy(order_by_args=ob_args, model=Buildings)
        query = current_session.query(Buildings).filter(Buildings.private_building == 0).order_by(Buildings.building_id).order_by(ob.column)
        buildings = paginate_query(query=query, paginate=pg_args['paginate'], page=pg_args['page'], limit=pg_args['limit'])
        building_id_list = [row.building_id for row in buildings]

        image_header_dict = {row.building_id: row.header_image_id for row in current_session.query(BuildingGraphicProfiles).filter(BuildingGraphicProfiles.building_id.in_(building_id_list)).all()}

        building_list = []
        for building in buildings:
            building_dict = {
                'building_id': building.building_id,
                'building_name': building.building_name,
                'header_image_id': str(image_header_dict[building.building_id]) if image_header_dict[building.building_id] is not None else None,
                'latitude': building.latitude,
                'longitude': building.longitude
            }
            building_list.append(building_dict)

        return building_list, 200

    except Exception as e:
        logger.exception(e)
        return error_response()


def update_graphic_profile(data):
    try:
        graphic_profile = current_session.query(BuildingGraphicProfiles).filter(BuildingGraphicProfiles.building_id == data['building_id']).one()
        if data['header_image']:
            header_image_id = upload_file(file_description='building_header_image', file=data['header_image'])
            graphic_profile.header_image_id = header_image_id

        graphic_profile.primary_color_hex = data['primary_color_hex']
        graphic_profile.accent_color_hex = data['accent_color_hex']
        graphic_profile.background_color_hex = data['background_color_hex']
        current_session.flush()
        current_session.commit()

        return success(data={
            'building_id': graphic_profile.building_id,
            'primary_color_hex': graphic_profile.primary_color_hex,
            'accent_color_hex': graphic_profile.accent_color_hex,
            'background_color_hex': graphic_profile.background_color_hex,
            'header_image_id': str(graphic_profile.header_image_id)
        })

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Building Graphic Profile does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()