from flask_restx import Resource, reqparse
from .service import *
from app.utils import error_response, check_page_args, input_validation_error, data_access_error, token_args, pagination_args, date_filter_args, order_by_args, search_string_args
from flask_jwt_extended import jwt_required
from app.support_classes import AuthenticationError
from app.authentication import check_entity_access

api = KiosksDTO.api

logger = api.logger

""" Standardised parameter setups """
token_args = token_args()
pagination_args = pagination_args()
date_filter_args = date_filter_args()
order_by_args = order_by_args()
search_string_args = search_string_args()


""" Namespace specific parameter setups """

get_kiosks_args = reqparse.RequestParser()
get_kiosks_args.add_argument('kiosk_id', type=str, required=True, help='Kiosk ID')



@api.route("/")
class Kiosks(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, KiosksDTO.post_kiosks_input, validate=False)
    def post(self):
        """ Create a new Kiosk - KIO-KIO-0 """
        try:
            data = api.payload
            check_entity_access(endpoint_id='KIO-KIO-0', entity_id=data['service_provider_id'])
            return create_kiosks(data)
        except Exception as e:
            logger.exception(e)
            return error_response()




