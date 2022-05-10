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

from .dto import OrdersDTO
api = OrdersDTO.api
logger = api.logger

from app.models.orders import Orders
from app.models.order_lines import OrderLines
from app.models.payment_methods import PaymentMethods
from app.models.payment_statuses import PaymentStatuses


def create_store_order(data):
    try:
        payment_method = current_session.query(PaymentMethods).filter(PaymentMethods.payment_method_id == data['payment_method_id']).one()

        order_id = str(uuid4())

        user_token = get_jwt()
        user_email = user_token['email']
        user_full_name = user_token['first_name'] + ' ' + user_token['last_name']

        order_total_amount_ex_vat = 0
        order_total_vat_amount = 0
        order_total_amount_incl_vat = 0

        for order_line in data['order_lines']:
            new_order_line = OrderLines(
                parent_order_id=order_id,
                product_id=order_line['product_id'],
                product_name=order_line['product_name'],
                product_price_ex_vat=order_line['product_price_ex_vat'],
                vat_rate=order_line['vat_rate'],
                product_price_incl_vat=order_line['product_price_ex_vat'] * (1 + order_line['vat_rate'] / 100),
                quantity=order_line['quantity'],
                total_amount_ex_vat=order_line['product_price_ex_vat'] * order_line['quantity'],
                total_amount_incl_vat=order_line['product_price_incl_vat'] * order_line['quantity'],
                created_at=timestamp_format(datetime.now())
            )

            order_total_amount_ex_vat += order_line['product_price_ex_vat'] * order_line['quantity']
            order_total_vat_amount += (order_line['product_price_incl_vat'] * order_line['quantity'] - order_line['product_price_ex_vat'] * order_line['quantity'])
            order_total_amount_incl_vat += order_line['product_price_incl_vat'] * order_line['quantity']
            current_session.add(new_order_line)

        new_order = Orders(
            order_id=order_id,
            store_id=data['store_id'],
            pos_id=data['pos_id'],
            total_amount_ex_vat=order_total_amount_ex_vat,
            total_vat_amount=order_total_vat_amount,
            total_amount_incl_vat=order_total_amount_incl_vat,
            payment_method_id=payment_method.payment_method_id,
            cash_order=payment_method.cash_order,
            user_id=data['user_id'],
            user_email=user_email,
            user_full_name=user_full_name,
            ordered_by=data['ordered_by'],
            created_at=timestamp_format(datetime.now())
        )
        current_session.add(new_order)

    except NoResultFound as e:
        logger.exception(e)
        return input_validation_error('Payment Method ID does not exist')
    except Exception as e:
        logger.exception(e)
        return error_response()



def get_orders(store_id, ob_args, search_string, pg_args, df_args):
    try:
        df = QueryDateFilter(date_args=df_args, date_column=Orders.created_at)
        ob = QueryOrderBy(order_by_args=ob_args, model=Orders)
        sf = QuerySearchFilter(search_string=search_string).all_columns(model=Orders)

        query = current_session.query(Orders).filter(Orders.store_id == store_id, *df.date_filter, or_(*sf)).order_by(ob.column)
        paginated_query = paginate_query(query=query, paginate=pg_args['paginate'], page=pg_args['page'], limit=pg_args['limit'])

        orders = paginated_query.items

        response_list = []
        for order in orders:
            order_dict = {
                'order_id': str(order.order_id),
                'user_full_name': order.user_full_name,
                'user_email': order.user_email,
                'created_at': timestamp_format(order.created_at)
            }
            response_list.append(order_dict)

        return {'page': paginated_query.page, 'total_pages': paginated_query.pages, 'total_items': paginated_query.total, 'orders': response_list}, 200

    except Exception as e:
        logger.exception(e)
        return error_response()
