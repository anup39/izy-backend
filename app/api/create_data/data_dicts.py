from app.utils import timestamp_format
from datetime import datetime
from app.models.building_graphic_profiles import BuildingGraphicProfiles
from app.models.buildings import Buildings
from app.models.licensees import Licensees
from app.models.building_modules import BuildingModules
from app.models.modules import Modules
from app.models.organisations import Organisations

from uuid import uuid4
from wonderwords import RandomWord
from random import randint
from names import get_first_name, get_last_name


""" Organisations Data """
org_0 = {
    'organisation_id': 'ORG-0',
    'organisation_name': 'Organisation-0',
    'organisation_number': '900800700',
    'registered_street_name': 'Kråkeveien',
    'registered_street_num': 1,
    'registered_city_name': 'Mordor',
    'registered_city_num': 3950,
    'post_box_num': '3950',
    'post_box_location_name': 'Mordoru',
    'post_box_city_num': 3950,
    'post_box_city_name': 'Mordor',
    'created_at': timestamp_format(datetime.now())
}
org_1 = {
    'organisation_id': 'ORG-1',
    'organisation_name': 'Organisation-1',
    'organisation_number': '911811711',
    'registered_street_name': 'Kråkeveien',
    'registered_street_num': 2,
    'registered_city_name': 'Mordor',
    'registered_city_num': 3950,
    'post_box_num': '3950',
    'post_box_location_name': 'Mordoru',
    'post_box_city_num': 3950,
    'post_box_city_name': 'Mordor',
    'created_at': timestamp_format(datetime.now())
}
org_2 = {
    'organisation_id': 'ORG-2',
    'organisation_name': 'Organisation-2',
    'organisation_number': '922822722',
    'registered_street_name': 'Kråkeveien',
    'registered_street_num': 3,
    'registered_city_name': 'Mordor',
    'registered_city_num': 3950,
    'post_box_num': '3950',
    'post_box_location_name': 'Mordoru',
    'post_box_city_num': 3950,
    'post_box_city_name': 'Mordor',
    'created_at': timestamp_format(datetime.now())
}

""" Licensees Data """
lic_0 = {
    'licensee_id': 'LIC-0',
    'licensee_name': 'EddyLic',
    'organisation_id': 'ORG-0',
    'created_at': timestamp_format(datetime.now())
}
lic_1 = {
    'licensee_id': 'LIC-1',
    'licensee_name': 'PattyLic',
    'organisation_id': 'ORG-1',
    'created_at': timestamp_format(datetime.now())
}
lic_2 = {
    'licensee_id': 'LIC-2',
    'licensee_name': 'ViggoLic',
    'organisation_id': 'ORG-2',
    'created_at': timestamp_format(datetime.now())
}

""" Buildings Data """
bui_0 = {
    'building_id': 'BUI-0',
    'building_name': 'EddyBui',
    'licensee_id': 'LIC-0',
    'user_app_self_registration': 1,
    'tenant_registration_code': 10001,
    'private_building': 0,
    'country': 'Norway',
    'country_code': 'NO',
    'postal_number': '3950',
    'address': 'Kråkeveien 1',
    'city': 'Mordor',
    'latitude': 60.0001,
    'longitude': 10.0001,
    'square_meters': 10000,
    'number_of_users': 100,
    'number_of_floors': 3,
    'created_at': timestamp_format(datetime.now())
}
bui_1 = {
    'building_id': 'BUI-1',
    'building_name': 'PattyBui',
    'licensee_id': 'LIC-1',
    'user_app_self_registration': 1,
    'tenant_registration_code': 10002,
    'private_building': 0,
    'country': 'Norway',
    'country_code': 'NO',
    'postal_number': '3950',
    'address': 'Kråkeveien 2',
    'city': 'Mordor',
    'latitude': 60.0001,
    'longitude': 10.0001,
    'square_meters': 10000,
    'number_of_users': 100,
    'number_of_floors': 3,
    'created_at': timestamp_format(datetime.now())
}
bui_2 = {
    'building_id': 'BUI-2',
    'building_name': 'ViggoBui',
    'licensee_id': 'LIC-2',
    'user_app_self_registration': 1,
    'tenant_registration_code': 10003,
    'private_building': 0,
    'country': 'Norway',
    'country_code': 'NO',
    'postal_number': '3950',
    'address': 'Kråkeveien 3',
    'city': 'Mordor',
    'latitude': 60.0001,
    'longitude': 10.0001,
    'square_meters': 10000,
    'number_of_users': 100,
    'number_of_floors': 3,
    'created_at': timestamp_format(datetime.now())
}

""" BuildingGraphicProfile Data """
bui_0_graphic_profile = {
    'building_id': 'BUI-0',
    'primary_color_hex': '#FF000',
    'accent_color_hex': '#001AFF',
    'background_color_hex': '#15FF00',
    'header_image_id': '13900af6-f648-4d03-aa4f-36956d08fe27'
}
bui_1_graphic_profile = {
    'building_id': 'BUI-1',
    'primary_color_hex': '#FF000',
    'accent_color_hex': '#001AFF',
    'background_color_hex': '#15FF00',
    'header_image_id': '4b476aaa-31a5-476c-95bd-f9d8623f88e8'
}
bui_2_graphic_profile = {
    'building_id': 'BUI-2',
    'primary_color_hex': '#FF000',
    'accent_color_hex': '#001AFF',
    'background_color_hex': '#15FF00',
    'header_image_id': '0284bf90-fa28-433f-8e7e-9879bb874086'
}

""" Modules Data """
mod_0 = {
    'module_id': 0,
    'module_name': 'Canteen',
    'module_description': 'Canteen Module',
    'created_at': timestamp_format(datetime.now())
}
mod_1 = {
    'module_id': 1,
    'module_name': 'Kiosk',
    'module_description': 'Kiosk Module',
    'created_at': timestamp_format(datetime.now())
}
mod_2 = {
    'module_id': 2,
    'module_name': 'Rent Space',
    'module_description': 'Rent Space Module',
    'created_at': timestamp_format(datetime.now())
}
mod_3 = {
    'module_id': 3,
    'module_name': 'Conference Meal',
    'module_description': 'Conference Meal Module',
    'created_at': timestamp_format(datetime.now())
}
mod_4 = {
    'module_id': 4,
    'module_name': 'Ad Hoc',
    'module_description': 'Ad Hoc Module',
    'created_at': timestamp_format(datetime.now())
}
mod_5 = {
    'module_id': 5,
    'module_name': 'News',
    'module_description': 'News Module',

}

""" BuildingModules Data """
building_module_00 = {
    'module_id': 0,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_01 = {
    'module_id': 1,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_02 = {
    'module_id': 2,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_03 = {
    'module_id': 3,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_04 = {
    'module_id': 4,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_05 = {
    'module_id': 5,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_10 = {
    'module_id': 0,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_11 = {
    'module_id': 1,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_12 = {
    'module_id': 2,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_13 = {
    'module_id': 3,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_14 = {
    'module_id': 4,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_15 = {
    'module_id': 5,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_20 = {
    'module_id': 0,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_21 = {
    'module_id': 1,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_22 = {
    'module_id': 2,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_23 = {
    'module_id': 3,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_24 = {
    'module_id': 4,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_25 = {
    'module_id': 5,
    'building_id': 'BUI-2',
    'active': 1
}

""" Data Dict Lists """
organisation_list = [org_0, org_1, org_2]
licensee_list = [lic_0, lic_1, lic_2]
building_list = [bui_0, bui_1, bui_2]
building_graphic_profile_list = [bui_0_graphic_profile, bui_1_graphic_profile, bui_2_graphic_profile]
building_module_list = [building_module_00, building_module_01, building_module_02, building_module_03, building_module_04, building_module_05, building_module_10, building_module_11, building_module_12, building_module_13, building_module_14, building_module_15, building_module_20, building_module_21, building_module_22, building_module_23, building_module_24, building_module_25]
module_list = [mod_0, mod_1, mod_2, mod_3, mod_4, mod_5]

""" Class and data dicts """
organisation_insert = {'class': Organisations, 'inserts': organisation_list}
licensee_insert = {'class': Licensees, 'inserts': licensee_list}
building_insert = {'class': Buildings, 'inserts': building_list}
building_graphic_profile_insert = {'class': BuildingGraphicProfiles, 'inserts': building_graphic_profile_list}
building_module_insert = {'class': BuildingModules, 'inserts': building_module_list}
module_insert = {'class': Modules, 'inserts': module_list}

def random_name():
    r = RandomWord()
    return r.word(include_parts_of_speech=["adjectives"]).capitalize() + r.word(include_parts_of_speech=["nouns"]).capitalize()

def create_dynamic_order(num_order_lines=3):
    stores = ['5c4c2fc0-4254-473c-8c0f-e235260fa8d2', 'c331dcd4-05f7-40d8-a689-34ccc400f7db', 'a05d63ce-9c85-4058-807b-7040d5b95c7f']
    poses = ['5c4c2fc0-4254-473c-8c0f-e235260fa8d1', 'c331dcd4-05f7-40d8-a689-34ccc400f7d1', 'a05d63ce-9c85-4058-807b-7040d5b95c71']
    order_lines = []
    store_pos_selector = randint(0, 2)
    vat_rates = [0, 15, 25]
    order_id = str(uuid4())
    created_at = f'{str(2022)}-0{str(randint(1, 9))}-1{str(randint(1, 9))} 12:00:00'

    total_amount_ex_vat = 0
    total_vat_amount = 0
    total_amount_incl_vat = 0

    for i in range(num_order_lines):
        product_price_ex_vat = randint(10, 30)
        vat_rate = vat_rates[randint(0, 2)]
        quantity = randint(1, 4)
        order_line = {
            'parent_order_id': order_id,
            'order_line_reference': None,
            'product_id': str(uuid4()),
            'product_name': random_name(),
            'product_price_ex_vat': product_price_ex_vat,
            'vat_rate': vat_rate,
            'product_price_incl_vat': product_price_ex_vat * (1 + vat_rate / 100),
            'quantity': quantity,
            'total_amount_ex_vat': product_price_ex_vat * quantity,
            'total_amount_incl_vat': product_price_ex_vat * (1 + vat_rate / 100) * quantity,
            'created_at': created_at
        }
        order_lines.append(order_line)
        total_amount_ex_vat += product_price_ex_vat * quantity
        total_vat_amount += (product_price_ex_vat * (1 + vat_rate / 100) * quantity - product_price_ex_vat * quantity)
        total_amount_incl_vat += product_price_ex_vat * (1 + vat_rate / 100) * quantity

    first_name = get_first_name()
    last_name = get_last_name()

    order = {
        'order_id': order_id,
        'store_id': stores[store_pos_selector],
        'pos_id': poses[store_pos_selector],
        'total_amount_ex_vat': total_amount_ex_vat,
        'total_vat_amount': total_vat_amount,
        'total_amount_incl_vat': total_amount_incl_vat,
        'payment_method_id': 1,
        'payment_status_id': 1,
        'cash_order': 1,
        'user_id': '33b86c10-418e-4790-ad03-16c2a4bfaab2',
        'user_email': first_name + '.' + last_name + '@mail.gnu',
        'user_full_name': first_name + ' ' + last_name,
        'created_at': created_at,
    }

    return order, order_lines




