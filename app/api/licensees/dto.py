from flask_restx import Namespace, fields


class LicenseesDto:

    api = Namespace("licensees", description="Licensees related operations")

    post_licensees_input = api.model(
        "post_licensees_input",
        {
            'organisation_id': fields.String,
            'licensee_name': fields.String,
            'create_building_access': fields.Integer
        }
    )

    put_licensees_input = api.model(
        "post_licensees_input",
        {
            'licensee_id': fields.String,
            'licensee_name': fields.String,
        }
    )

