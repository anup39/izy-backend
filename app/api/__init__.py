import os
from flask_restx import Api
from flask import Blueprint
from config import Config

from .organisations.controller import api as organisation_ns
from .licensees.controller import api as licensees_ns
from .buildings.controller import api as buildings_ns
from .create_data.controller import api as create_data_ns
from .orders.controller import api as orders_ns


api_bp = Blueprint("api", __name__)
api = Api(api_bp, title=Config.SWAGGER_TITLE, description=Config.SWAGGER_DESCRIPTION, version=Config.SWAGGER_VERSION)

# API namespaces
api.add_namespace(create_data_ns)
api.add_namespace(organisation_ns)
api.add_namespace(licensees_ns)
api.add_namespace(buildings_ns)
api.add_namespace(orders_ns)

