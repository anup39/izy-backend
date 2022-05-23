from flask_restx import Resource, reqparse
from .service import *
from flask import Flask
from app.authentication import check_entity_access
from app.utils import error_response, input_validation_error, data_access_error, check_page_args, token_args, pagination_args, date_filter_args, order_by_args
from app.support_classes import AuthenticationError
from flask_jwt_extended import jwt_required
from .dto import BuildingsDTO
# import logging
api = BuildingsDTO.api
# app = Flask(__name__)
logger = api.logger

""" Standardised parameter setups """
token_args = token_args()
pagination_args = pagination_args()
date_filter_args = date_filter_args()
order_by_args = order_by_args()


""" Namespace specific parameter setups """

building_id_args = reqparse.RequestParser()
building_id_args.add_argument('building_id', type=str, required=True, help='Building id')

building_module_id_args = reqparse.RequestParser()
building_module_id_args.add_argument('building_module_id', type=str, required=True, help='Building module id')

# logging.basicConfig(level=logging.DEBUG)
@api.route("/")
class BuildingsRoot(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args,building_id_args)
    def get(self):
        """ Get building data - TPL-BUI-0 """
        print("Inside building get")
        try:
            args = building_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-BUI-0', entity_id=args['building_id'])
            return get_building_data(args['building_id'])

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, BuildingsDTO.post_buildings_input, validate=True)
    @api.expect( BuildingsDTO.post_buildings_input, validate=True)
    def post(self):
        """ Create new building from licensee - TPL-BUI-1 """
        try:
            data = api.payload
            # check_entity_access(endpoint_id='TPL-BUI-1', entity_id=data['licensee_id'])
            print("the entity check is passed")
            return create_building(data)

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, BuildingsDTO.put_buildings_input)
    def put(self):
        """ Update building base data - TPL-BUI-2 """
        try:
            data = api.payload
            check_entity_access(endpoint_id='TPL-BUI-2', entity_id=data['licensee_id'])
            return update_building_base_data(data)

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, building_id_args)
    def delete(self):
        """ Soft delete building - TPL-BUI-3 """
        try:
            args = building_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-BUI-3', entity_id=args['building_id'])
            return soft_delete_building(args['building_id'])

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()




class BuildingsModules(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, building_id_args)
    def get(self):
        """ Get modules for a building - TPL-BUI-4 """
        try:
            args = building_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-BUI-4', entity_id=args['building_id'])
            return get_building_modules(args['building_id'])

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()



    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, BuildingsDTO.put_module_input)
    def put(self):
        """ Change module state for building - TPL-BUI-5 """
        try:
            data = api.payload
            return update_building_module_state(data=data, endpoint_id='ENT-5')

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()



@api.route("/public")
class BuildingsPublic(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, pagination_args, order_by_args)


    def get(self):
        """ Get all non-private buildings - TPL-BUI-6 """
        try:
            pg_args = pagination_args.parse_args()
            ob_args = order_by_args.parse_args()
            check_page_args(pg_args)
            return get_all_public_buildings(pg_args=pg_args, ob_args=ob_args)

        except ValueError as e:
            logger.exception(e)
            return input_validation_error('Pagination is active, and page or limit is of wrong format')
        except Exception as e:
            logger.exception(e)
            return error_response()


@api.route("/graphic-profile")
class BuildingsGraphicProfile(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, BuildingsDTO.put_graphic_profile_input)
    def put(self):
        """ Update building graphic profile - TPL-BUI-7 """
        try:
            data = api.payload
            check_entity_access(endpoint_id='TPL-BUI-7', entity_id=data['building_id'])
            return update_graphic_profile(data)

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()

