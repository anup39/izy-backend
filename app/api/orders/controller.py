from flask_restx import Resource, reqparse
from .service import *
from app.utils import error_response, check_page_args, input_validation_error, data_access_error, token_args, pagination_args, date_filter_args, order_by_args, search_string_args
from flask_jwt_extended import jwt_required
from app.support_classes import AuthenticationError

api = OrdersDTO.api

logger = api.logger

""" Standardised parameter setups """
token_args = token_args()
pagination_args = pagination_args()
date_filter_args = date_filter_args()
order_by_args = order_by_args()
search_string_args = search_string_args()


""" Namespace specific parameter setups """

get_orders_args = reqparse.RequestParser()
get_orders_args.add_argument('store_id', type=str, required=True, help='Store ID')



@api.route("/")
class Orders(Resource):
    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, OrdersDTO.post_orders_input, validate=False)
    def post(self):
        """ Create a new store order - TPL-ORD-0 """
        try:
            data = api.payload
            return create_store_order(data)
        except Exception as e:
            logger.exception(e)
            return error_response()


    @jwt_required()
    @api.doc(responses={200: "Success"})
    @api.expect(token_args, pagination_args, order_by_args, date_filter_args, get_orders_args, search_string_args)
    def get(self):
        """ Get orders for store - TPL-ORD-1 """
        try:
            args = get_orders_args.parse_args()
            pg_args = pagination_args.parse_args()
            ob_args = order_by_args.parse_args()
            df_args = date_filter_args.parse_args()

            check_page_args(pg_args)
            return get_orders(store_id=args['store_id'], search_string=args['search_string'], ob_args=ob_args, df_args=df_args, pg_args=pg_args)


        except AuthenticationError as e:
            logger.exception(e)
            return data_access_error()
        except ValueError as e:
            logger.exception(e)
            return input_validation_error('Check pagination args')
        except Exception as e:
            logger.exception(e)
            return error_response()

