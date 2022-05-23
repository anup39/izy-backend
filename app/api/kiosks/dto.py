from flask_restx import Namespace, fields


class KiosksDTO:

    api = Namespace("kiosks", description="kiosks related operations")

    post_kiosks_input = api.model(
        "post_kiosks_input",
        {
            'kiosk_name': fields.String,
            'description': fields.String,
            'service_provider_id': fields.String,
            'building_module_id': fields.Integer,
            'thumbnail_image_id': fields.String,
            'header_image_id': fields.String,
            'service_provider_internal_id': fields.String,

        }
    )



