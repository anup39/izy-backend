from app.utils import timestamp_format
from datetime import datetime

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

bui_0 = {
    'building_id': 'BUI-0',
    'building_name': 'EddyBui',
    'licensee_id': 'LIC-0',
    'user_app_self_registration': 1,
    'tenant_registration_code': 10001,
    'private_building': 0,
    'postal_address': {
        'country': 'Norway',
        'country_code': 'NO',
        'postal_number': '3950',
        'address': 'Kråkeveien 1',
        'city': 'Mordor',
    },
    'graphic_profile': bui_1_graphic_profile,
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
    'postal_address': {
        'country': 'Norway',
        'country_code': 'NO',
        'postal_number': '3950',
        'address': 'Kråkeveien 2',
        'city': 'Mordor',
    },
    'graphic_profile': bui_2_graphic_profile,
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
    'postal_address': {
        'country': 'Norway',
        'country_code': 'NO',
        'postal_number': '3950',
        'address': 'Kråkeveien 3',
        'city': 'Mordor',
    },
    'graphic_profile': bui_2_graphic_profile,
    'latitude': 60.0001,
    'longitude': 10.0001,
    'square_meters': 10000,
    'number_of_users': 100,
    'number_of_floors': 3,
    'created_at': timestamp_format(datetime.now())
}



building_module_00 = {
    'building_module_id': 0,
    'module_id': 0,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_01 = {
    'building_module_id': 1,
    'module_id': 1,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_02 = {
    'building_module_id': 2,
    'module_id': 2,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_03 = {
    'building_module_id': 3,
    'module_id': 3,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_04 = {
    'building_module_id': 4,
    'module_id': 4,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_05 = {
    'building_module_id': 5,
    'module_id': 5,
    'building_id': 'BUI-0',
    'active': 1
}
building_module_10 = {
    'building_module_id': 6,
    'module_id': 0,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_11 = {
    'building_module_id': 7,
    'module_id': 1,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_12 = {
    'building_module_id': 8,
    'module_id': 2,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_13 = {
    'building_module_id': 9,
    'module_id': 3,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_14 = {
    'building_module_id': 10,
    'module_id': 4,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_15 = {
    'building_module_id': 11,
    'module_id': 5,
    'building_id': 'BUI-1',
    'active': 1
}
building_module_20 = {
    'building_module_id': 12,
    'module_id': 0,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_21 = {
    'building_module_id': 13,
    'module_id': 1,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_22 = {
    'building_module_id': 14,
    'module_id': 2,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_23 = {
    'building_module_id': 15,
    'module_id': 3,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_24 = {
    'building_module_id': 16,
    'module_id': 4,
    'building_id': 'BUI-2',
    'active': 1
}
building_module_25 = {
    'building_module_id': 17,
    'module_id': 5,
    'building_id': 'BUI-2',
    'active': 1
}

rom_00 = {
    'room_id': 'ROM-0',
    'room_name': 'Room 00',
    'building_id': 'BUI-0',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}
rom_01 = {
    'room_id': 'ROM-1',
    'room_name': 'Room 01',
    'building_id': 'BUI-0',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}
rom_02 = {
    'room_id': 'ROM-2',
    'room_name': 'Room 02',
    'building_id': 'BUI-0',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}
rom_10 = {
    'room_id': 'ROM-3',
    'room_name': 'Room 10',
    'building_id': 'BUI-1',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}
rom_11 = {
    'room_id': 'ROM-4',
    'room_name': 'Room 11',
    'building_id': 'BUI-1',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}
rom_12 = {
    'room_id': 'ROM-5',
    'room_name': 'Room 12',
    'building_id': 'BUI-1',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}
rom_20 = {
    'room_id': 'ROM-6',
    'room_name': 'Room 20',
    'building_id': 'BUI-2',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}
rom_21 = {
    'room_id': 'ROM-7',
    'room_name': 'Room 21',
    'building_id': 'BUI-2',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}
rom_22 = {
    'room_id': 'ROM-8',
    'room_name': 'Room 22',
    'building_id': 'BUI-2',
    'floor': 1,
    'created_at': timestamp_format(datetime.now())
}

building_area_00 = {
    'area_id': 'ARE-0',
    'area_name': 'Area 00',
    'building_id': 'BUI-0',
    'created_at': timestamp_format(datetime.now())
}
building_area_10 = {
    'area_id': 'ARE-1',
    'area_name': 'Area 10',
    'building_id': 'BUI-1',
    'created_at': timestamp_format(datetime.now())
}
building_area_20 = {
    'area_id': 'ARE-2',
    'area_name': 'Area 20',
    'building_id': 'BUI-2',
    'created_at': timestamp_format(datetime.now())
}

room_area_relation_00 = {
    'area_id': 'ARE-0',
    'room_id': 'ROM-0'
}

room_area_relation_11 = {
    'area_id': 'ARE-1',
    'room_id': 'ROM-1'
}
room_area_relation_22 = {
    'area_id': 'ARE-2',
    'room_id': 'ROM-2'
}

area_floor_relation_01 = {
    'area_id': 'ARE-0',
    'floor': 1
}
area_floor_relation_11 = {
    'area_id': 'ARE-1',
    'floor': 1
}
area_floor_relation_21 = {
    'area_id': 'ARE-2',
    'floor': 1
}

building_contact_00 = {
    'contact_id': 'CON-0',
    'contact_name': 'Kaare Bahåret',
    'contact_email': 'kaare.bahaaret@bui.gnu',
    'contact_phone': '90101010',
    'opening_hours': 'Åpningstider ja',
    'role_description': 'Vaktmester',
    'building_id': 'BUI-0',
    'created_at': timestamp_format(datetime.now())
}
building_contact_01 = {
    'contact_id': 'CON-1',
    'contact_name': 'Vigdis Vekkimellom',
    'contact_email': 'Vigdis.vekkimellom@bui.gnu',
    'contact_phone': '90202020',
    'opening_hours': 'Åpningstider ja',
    'role_description': 'Vaskeansvarlig',
    'building_id': 'BUI-0',
    'created_at': timestamp_format(datetime.now())
}
building_contact_10 = {
    'contact_id': 'CON-2',
    'contact_name': 'Børre Basketak',
    'contact_email': 'borre.basketak@bui.gnu',
    'contact_phone': '90303030',
    'opening_hours': 'Åpningstider ja',
    'role_description': 'Vaktmester',
    'building_id': 'BUI-1',
    'created_at': timestamp_format(datetime.now())
}
building_contact_11 = {
    'contact_id': 'CON-3',
    'contact_name': 'Turid Trangsynt',
    'contact_email': 'turid.trangsynt@bui.gnu',
    'contact_phone': '90404040',
    'opening_hours': 'Åpningstider ja',
    'role_description': 'Vaskeansvarlig',
    'building_id': 'BUI-1',
    'created_at': timestamp_format(datetime.now())
}
building_contact_20 = {
    'contact_id': 'CON-4',
    'contact_name': 'Birger Bunkersprenger',
    'contact_email': 'birger.Bunkersprenger@bui.gnu',
    'contact_phone': '90505050',
    'opening_hours': 'Åpningstider ja',
    'role_description': 'Vaktmester',
    'building_id': 'BUI-2',
    'created_at': timestamp_format(datetime.now())
}
building_contact_21 = {
    'contact_id': 'CON-5',
    'contact_name': 'Margot Mellomsprekk',
    'contact_email': 'margot.mellomsprekk@bui.gnu',
    'contact_phone': '90606060',
    'opening_hours': 'Åpningstider ja',
    'role_description': 'Vaskeansvarlig',
    'building_id': 'BUI-2',
    'created_at': timestamp_format(datetime.now())
}

bap_00 = {
    'application_id': 'BAP-0',
    'application_name': 'Parks and Recreation Fixer',
    'url_1': 'www.pars.gnu',
    'url_2': 'appstore.pars.gnu',
    'url_3': 'googleplay.pars.gnu',
    'building_id': 'BUI-0',
    'created_at': timestamp_format(datetime.now())
}
bap_10 = {
    'application_id': 'BAP-1',
    'application_name': 'Teeth Icing Helper',
    'url_1': 'www.teeth.gnu',
    'url_2': 'appstore.teeth.gnu',
    'url_3': 'googleplay.teeth.gnu',
    'building_id': 'BUI-1',
    'created_at': timestamp_format(datetime.now())
}
bap_20 = {
    'application_id': 'BAP-2',
    'application_name': 'Chimney Sweepz',
    'url_1': 'www.chimney.gnu',
    'url_2': 'appstore.chimney.gnu',
    'url_3': 'googleplay.chimney.gnu',
    'building_id': 'BUI-2',
    'created_at': timestamp_format(datetime.now())
}