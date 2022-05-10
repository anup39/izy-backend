from flask_restx import Namespace, fields


class OrdersDTO:

    api = Namespace("orders", description="orders related operations")

    order_line_nested = api.model(
        "order_line_input",
        {
            'product_id': fields.String,
            'product_name': fields.String,
            'product_price_ex_vat': fields.Float,
            'vat_rate': fields.Float,
            'quantity': fields.Float,
        }
    )

    post_orders_input = api.model(
        "post_orders_input",
        {
            'payment_method_id': fields.Integer,
            'user_id': fields.String,
            'ordered_by': fields.String,
            'store_id': fields.String,
            'pos_id': fields.String,
            'order_lines': fields.Nested(order_line_nested)
        }
    )


