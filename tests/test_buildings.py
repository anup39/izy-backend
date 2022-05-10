import unittest
import os
from tests.utils.endpoints.buildings import *
from tests.utils.data_dicts.buildings import *
from tests.utils.base import BaseTestCase
import requests
from flask import current_app
from app import create_app
from config import basedir
from utils.common import login, response_data


class TestBuildingsNamespace(BaseTestCase):
    # TMP-ENT-0
    def test_post_buildings(self):
        token = login().json()

        # Insert first building
        resp = post_buildings(self, token, bui_0)
        self.assertEquals(resp.status_code, 200)

        # Insert building without LIC access
        resp = post_buildings(self, token, bui_2)
        self.assertEquals(resp.status_code, 400)
        self.assertEquals(response_data(resp)['status'], 'Data Access Error')

    # TMP-ENT-1
    def test_get_buildings(self):
        token = login().json()

        # Insert building
        post_buildings(self, token, bui_0)

        # Get building data
        resp = get_buildings(self, token, building_id=bui_0['building_id'])
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(response_data(resp)['building_name'], 'EddyBui')

    # TMP-ENT-2
    def test_put_buildings(self):
        token = login().json()

        # Insert building
        post_buildings(self, token, bui_0)
        resp = get_buildings(self, token, building_id=bui_0['building_id'])
        resp_data = response_data(resp)

        # Edit payload for PUT request
        resp_data['building_id'] = bui_0['building_id']
        resp_data['building_name'] = 'New Name'

        # Edit building
        resp = put_buildings(self, token, resp_data)
        self.assertEquals(resp.status_code, 200)
        resp = get_buildings(self, token, building_id=bui_0['building_id'])
        self.assertEquals(response_data(resp)['building_name'], 'New Name')

    # TMP-ENT-3
    def test_delete_buildings(self):
        token = login().json()

        # Insert building
        post_buildings(self, token, bui_0)
        resp = get_buildings(self, token, building_id=bui_0['building_id'])
        self.assertEquals(resp.status_code, 200)

        # Delete building
        resp = delete_buildings(self, token, building_id=bui_0['building_id'])
        self.assertEquals(resp.status_code, 200)

    # TMP-ENT-4
    def test_get_buildings_modules(self):
        token = login().json()

        # Insert building
        post_buildings(self, token, 'BUI-0')

        # Get building modules
        resp = get_buildings_modules(self, token, building_id=bui_0['building_id'])
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(len(response_data(resp)), 0)

    def test_print(self):
        print('WORKS')






