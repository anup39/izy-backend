from flask_restx import Namespace, fields
from app.support_classes import NullableString


class CreateDataDto:

    api = Namespace(
        "data",
        description="Create data."
    )