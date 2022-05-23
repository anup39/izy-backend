from flask_restx import Resource, reqparse
from .service import *
from app.utils import error_response, input_validation_error, data_access_error, token_args, pagination_args, date_filter_args, order_by_args
from app.authentication import check_entity_access
from flask_jwt_extended import jwt_required
from app.support_classes import AuthenticationError

api = OrganisationDto.api

logger = api.logger

""" Standardised parameter setups """
token_args = token_args()
pagination_args = pagination_args()
date_filter_args = date_filter_args()
order_by_args = order_by_args()

""" Namespace specific parameter setups """

org_id_args = reqparse.RequestParser()
org_id_args.add_argument('organisation_id', type=str, required=True, help='organisation id')

org_number_args = reqparse.RequestParser()
org_number_args.add_argument('organisation_number', type=str, required=True, help='Registered Organisation Number in BRREG')



@api.route("/")
class OrganisationPost(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, OrganisationDto.post_organisations_input, validate=True)
    def post(self):
        """ Create a new organisation - TPL-ORG-0 """
        try:
            data = api.payload
            return add_organisation(data)
        except Exception as e:
            logger.exception(e)
            return error_response()

    
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, org_id_args)
    def get(self):
        """ Get organisation base data and organisation_instances - TPL-ORG-1 """
        try:
            args = org_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-ORG-1', entity_id=args['organisation_id'])
            return get_organisation_data(args['organisation_id'])

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, OrganisationDto.put_organisations_input)
    def put(self):
        """ Update organisation - TPL-ORG-2 """
        try:
            data = api.payload
            check_entity_access(endpoint_id='TPL-ORG-2', entity_id=data['organisation_id'])
            return update_organisation_data(data)

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, org_id_args)
    def delete(self):
        """ Delete organisation - TPL-ORG-3 """
        try:
            args = org_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-ORG-3', entity_id=args['organisation_id'])
            return soft_delete_organisation(args['organisation_id'])

        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except Exception as e:
            logger.exception(e)
            return error_response()



@api.route("/registry-data")
class OrganisationGetRegistryData(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, org_number_args)
    def get(self):
        """ Get base organisation data from BRREG - TPL-ORG-4 """
        try:
            args = org_number_args.parse_args()
            # Validate organisation number format
            try:
                int(args['organisation_number'])
            except ValueError as e:
                logger.exception(e)
                return input_validation_error(f'Format of organisation number is invalid: {args["organisation_number"]}')

            return get_organisation_registry_data(args['organisation_number'])

        except Exception as e:
            logger.exception(e)
            return error_response()



@api.route("/licensees")
class OrganisationGetLicensees(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, org_id_args)
    def get(self):
        """ Get all licensees from organisation - TPL-ORG-5 """
        try:
            args = org_id_args.parse_args()
            check_entity_access(endpoint_id='TPL-ORG-5', entity_id=args['organisation_id'])
            return get_organisation_licensees(args['organisation_id'])

        except Exception as e:
            logger.exception(e)
            return error_response()
