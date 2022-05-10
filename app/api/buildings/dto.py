from flask_restx import Namespace, fields



class BuildingsDTO:

    api = Namespace("buildings", description="Building related operations")

    postal_address_nested = api.model(
        "postal_address_nested",
        {
            'country': fields.String,
            'country_code': fields.String,
            'postal_number': fields.String,
            'address': fields.String,
            'city': fields.String,
        }
    )

    put_module_input = api.model(
        "put_module_input",
        {
            'building_module_id': fields.Integer,
            'active': fields.Integer
        }
    )

    graphic_profile_nested = api.model(
        "graphic_profile_nested",
        {
            'primary_color_hex': fields.String,
            'accent_color_hex': fields.String,
            'background_color_hex': fields.String,
            'header_image': fields.String
        }
    )

    put_graphic_profile_input = api.model(
        "put_graphic_profile_input",
        {
            'building_id': fields.String,
            'primary_color_hex': fields.String,
            'accent_color_hex': fields.String,
            'background_color_hex': fields.String,
            'header_image': fields.String
        }
    )

    post_external_application_input = api.model(
        "post_external_application_input",
        {
            'building_id': fields.String,
            'application_name': fields.String,
            'url_1': fields.String,
            'url_2': fields.String,
            'url_3': fields.String,
            'image': fields.String
        }
    )

    put_external_application_input = api.model(
        "put_external_application_input",
        {
            'application_id': fields.String,
            'application_name': fields.String,
            'url_1': fields.String,
            'url_2': fields.String,
            'url_3': fields.String,
            'image': fields.String
        }
    )

    post_contacts_input = api.model(
        "post_contacts_input",
        {
            'contact_name': fields.String,
            'contact_email': fields.String,
            'contact_phone': fields.String,
            'opening_hours': fields.String,
            'role_description': fields.String,
            'building_id': fields.String
        }
    )

    put_contacts_input = api.model(
        "put_contacts_input",
        {
            'contact_id': fields.String,
            'contact_name': fields.String,
            'contact_email': fields.String,
            'contact_phone': fields.String,
            'opening_hours': fields.String,
            'role_description': fields.String,
        }
    )
    post_buildings_input = api.model(
        "post_buildings_input",
        {
            'building_name': fields.String,
            'licensee_id': fields.String,
            'user_app_self_registration': fields.Integer,
            'private_building': fields.Integer,
            'postal_address': fields.Nested(postal_address_nested),
            'graphic_profile': fields.Nested(graphic_profile_nested),
            'latitude': fields.Float,
            'longitude': fields.Float,
            'square_meters': fields.Integer,
            'number_of_users': fields.Integer,
            'number_of_floors': fields.Integer
        }
    )

    put_buildings_input = api.model(
        "put_buildings_input",
        {
            'building_id': fields.Integer,
            'building_name': fields.String,
            'user_app_self_registration': fields.Integer,
            'private_building': fields.Integer,
            'postal_address': fields.Nested(postal_address_nested),
            'latitude': fields.Float,
            'longitude': fields.Float,
            'square_meters': fields.Integer,
            'number_of_users': fields.Integer,
            'number_of_floors': fields.Integer
        }
    )

