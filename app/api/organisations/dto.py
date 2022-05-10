import logging
import os
from flask_restx import Namespace, fields


class OrganisationDto:

    api = Namespace("organisations", description="organisations related operations")

    post_organisations_input = api.model(
        "post_organisations_input",
        {
            'organisation_number': fields.String,
            'organisation_name': fields.String,
            'address': fields.String,
            'postal_code': fields.String,
            'city': fields.String
        }
    )

    put_organisations_input = api.model(
        "put_organisations_input",
        {
            'organisation_id': fields.String,
            'organisation_name': fields.String,
            'address': fields.String,
            'postal_code': fields.String,
            'city': fields.String
        }
    )

