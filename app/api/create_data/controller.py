from flask_restx import Resource
from flask import current_app as app
from .service import *
from .dto import CreateDataDto
import logging
from app.utils import error_response
from sqlalchemy.inspection import inspect
from app.models.orders import Orders


api = CreateDataDto.api

logger = api.logger

@api.route("/")
class Test(Resource):
    def get(self):
        try:
            model = Orders
            types = []
            for column in model.__table__.columns:
                types.append(str(column.type))

            return types, 200
        except Exception as e:
            logger.exception(e)
            return error_response()


@api.route("/data/fill-all")
class CreateTestData(Resource):
    @api.doc(responses={200: 'OK'})
    def post(self):
        """ Create test data in all tables """
        try:
            return create_stock_data()
        except Exception as e:
            logger.exception(e)
            return error_response()



@api.route("/create-orders")
class CreateTestData(Resource):
    @api.doc(responses={200: 'OK'})
    def post(self):
        """ Create orders """
        try:
            return create_orders(200)
        except Exception as e:
            logger.exception(e)
            return error_response()

