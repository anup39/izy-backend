import requests
import json

def login():
    username = 'mongo@email.gnu'
    password = 'svein'
    url = 'http://127.0.0.1:5000/api/users/login'
    return requests.post(url=url, json={'username': username, 'password': password})


def response_data(response):
    return json.loads(response.data)