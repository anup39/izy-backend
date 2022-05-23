import json

# TMP-ENT-1
def post_buildings(self, token, data):
    return self.client.post(
        "/api/buildings/",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-0
def get_buildings(self, token, building_id):
    return self.client.get(
        "/api/buildings/",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-2
def put_buildings(self, token, data):
    return self.client.put(
        "/api/buildings/",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-3
def delete_buildings(self, token, building_id):
    return self.client.delete(
        "/api/buildings/",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-4
def get_buildings_modules(self, token, building_id):
    return self.client.get(
        "/api/buildings/modules",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-5
def put_buildings_modules(self, token, data):
    return self.client.put(
        "/api/buildings/modules",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-6
def get_buildings_external_applications(self, token, building_id):
    return self.client.get(
        "/api/buildings/external-applications",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-7
def post_buildings_external_applications(self, token, data):
    return self.client.post(
        "/api/buildings/external-applications",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-8
def put_buildings_external_applications(self, token, data):
    return self.client.put(
        "/api/buildings/external-applications",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-9
def get_buildings_contacts(self, token, building_id):
    return self.client.get(
        "/api/buildings/contacts",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-10
def post_buildings_contacts(self, token, data):
    return self.client.post(
        "/api/buildings/contacts",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-11
def put_buildings_contacts(self, token, data):
    return self.client.put(
        "/api/buildings/contacts",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-12
def get_buildings_modules_service_providers(self, token, building_id):
    return self.client.get(
        "/api/buildings/modules/service-providers",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-13
def post_buildings_modules_service_providers(self, token, data):
    return self.client.post(
        "/api/buildings/modules/service-providers",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-14
def delete_buildings_modules_service_providers(self, token, data):
    return self.client.elete(
        "/api/buildings/modules/service-providers",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-15
def get_buildings_public(self, token, paginate, page, limit):
    return self.client.get(
        "/api/buildings/public",
        query_string=(
            {
                'paginate': paginate,
                'page': page,
                'limit': limit
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-16
def put_buildings_graphic_profile(self, token, data):
    return self.client.put(
        "/api/buildings/graphic-profile",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-17
def get_buildings_customers(self, token, building_id):
    return self.client.get(
        "/api/buildings/customers",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-18
def post_buildings_customers(self, token, data):
    return self.client.post(
        "/api/buildings/customers",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-19
def delete_buildings_customers(self, token, building_id, customer_id):
    return self.client.delete(
        "/api/buildings/customers",
        query_string=(
            {
                'building_id': building_id,
                'customer_id': customer_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-20
def get_buildings_areas(self, token, area_id):
    return self.client.get(
        "/api/buildings/areas",
        query_string=(
            {
                'area_id': area_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-21
def post_buildings_areas(self, token, data):
    return self.client.post(
        "/api/buildings/areas",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-22
def put_buildings_areas(self, token, data):
    return self.client.put(
        "/api/buildings/areas",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-23
def delete_buildings_areas(self, token, area_id):
    return self.client.delete(
        "/api/buildings/customers",
        query_string=(
            {
                'area_id': area_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-24
def get_buildings_areas_building(self, token, building_id):
    return self.client.get(
        "/api/buildings/areas/building",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-25
def get_buildings_rooms(self, token, room_id):
    return self.client.get(
        "/api/buildings/rooms",
        query_string=(
            {
                'room_id': room_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-26
def post_buildings_rooms(self, token, data):
    return self.client.post(
        "/api/buildings/rooms",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-27
def put_buildings_rooms(self, token, data):
    return self.client.put(
        "/api/buildings/rooms",
        data=json.dumps(data),
        content_type="application/json",
        headers={"Authorization": 'Bearer ' + token}
    )

# TMP-ENT-28
def delete_buildings_rooms(self, token, room_id):
    return self.client.delete(
        "/api/buildings/rooms",
        query_string=(
            {
                'room_id': room_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-29
def get_buildings_rooms_area(self, token, area_id):
    return self.client.get(
        "/api/buildings/rooms/area",
        query_string=(
            {
                'area_id': area_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})

# TMP-ENT-30
def get_buildings_rooms_building(self, token, building_id):
    return self.client.get(
        "/api/buildings/rooms/building",
        query_string=(
            {
                'building_id': building_id
            }
        ),
        headers={"Authorization": 'Bearer ' + token})
