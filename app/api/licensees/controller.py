from flask_restx import Resource, reqparse
from app.utils import data_access_error
from app.support_classes import AuthenticationError
from flask_jwt_extended import jwt_required
from .service import *
from app.authentication import check_entity_access


api = LicenseesDto.api

logger = api.logger

""" Token parameter setup sourced from header: Authorization"""
token_args = reqparse.RequestParser()
token_args.add_argument('Authorization', type=str, location='headers', help='Bearer Token', required=True)

""" Pagination parameter setup """
pagination_args = reqparse.RequestParser()
pagination_args.add_argument('paginate', type=int, required=True, help='Turn pagination on or off')
pagination_args.add_argument('page', type=int, required=False, help='Page number to fetch')
pagination_args.add_argument('limit', type=int, required=False, help='Page size')

""" Date filter args """
date_filter_args = reqparse.RequestParser()
date_filter_args.add_argument('date_from', type=str, required=False, help='YYYY-MM-DD')
date_filter_args.add_argument('date_to', type=str, required=False, help='YYYY-MM-DD')

""" Order-By args """
order_by_args = reqparse.RequestParser()
order_by_args.add_argument('order_by', type=str, required=False, help='Set field to order by')
order_by_args.add_argument('order_direction', type=str, required=False, help='Order direction: asc/desc')


""" Namespace specific parameter setups """

licensee_id_args = reqparse.RequestParser()
licensee_id_args.add_argument('licensee_id', type=str, required=True, help='organisation id')


@api.route("/")
class LicenseesRoot(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, LicenseesDto.post_licensees_input, validate=True)
    def post(self):
        """ Create new licensee from organisation - TPL-LIC-0 """
        try:
            data = api.payload
            check_entity_access(endpoint_id='TPL-LIC-0', entity_id=data['organisation_id'])
            return create_licensee(data)

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, licensee_id_args)
    def get(self):
        """ Get licensee data - TPL-LIC-1 """
        try:
            args = licensee_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-LIC-1', entity_id=args['licensee_id'])
            return get_licensee_data(args['licensee_id'])

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, LicenseesDto.put_licensees_input)
    def put(self):
        """ Update licensee data - TPL-LIC-2 """
        try:
            data = api.payload
            check_entity_access(endpoint_id='TPL-LIC-2', entity_id=data['licensee_id'])
            return update_licensee_base_data(data)

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, licensee_id_args)
    def delete(self):
        """ Delete licensee. N/A if child buildings exists - TPL-LIC-3 """
        try:
            args = licensee_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-LIC-3', entity_id=args['licensee_id'])
            return soft_delete_licensee(args['licensee_id'])

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()



@api.route("/buildings")
class LicenseesGetBuildings(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, licensee_id_args)
    def get(self):
        """ Get all buildings for licensee - TPL-LIC-4 """
        try:
            args = licensee_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-LIC-4', entity_id=args['licensee_id'])
            return get_licensee_buildings(args['licensee_id'])

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()
