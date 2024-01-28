import requests
import time


def create_request_body(endpoint):
    if endpoint == '/alerts':
        json_data = {"idAlert": 30, "idSensor": 2, "description": "Alerta de temperatura",
                     "cleared": True}
    elif endpoint == '/sensors':
        json_data = {"idSensor": 3, "idLocation": 2, "name": "Sensor de movimento",
                     "unit": "Celsius"}
    elif endpoint == '/units':
        json_data = {"unit": "CelsiusFarenheit", "description": "Alerta temperatura"}
    elif endpoint == '/locations':
        json_data = {"idLocation": 0, "name": "Albufeira", "description": "Gambelas"}
    elif endpoint == '/readings':
        json_data = {"idReading": 3, "idSensor": 3, "value": 26.6}
    else:
        json_data = ""
    return json_data


def call_endpoint():
    file_name = "endpoints.csv"
    file = open(file_name, "r")
    lines = file.readlines()
    base_url = "http://127.0.0.1:5000"
    for line in lines:
        method, endpoint = line.strip().split(',')
        if method == "GET":
            request_url = base_url + endpoint.strip()
            request = requests.get(request_url)
            response = request.text
            print(response)
        if method == "POST":
            endpoint = endpoint.strip()
            request_url = base_url + endpoint
            json_data = create_request_body(endpoint)
            request = requests.post(request_url, json=json_data)
            response = request.text
            print(response)
            time.sleep(3)
        if method == "PUT":
            endpoint = endpoint.strip()
            request_url = base_url + endpoint
            json_data = create_request_body(endpoint)
            request = requests.put(request_url, json=json_data)
            response = request.text
            return response
        if method == "DELETE":
            request_url = base_url + endpoint.strip()
            response = requests.delete(request_url)
            print(response.text)


call_endpoint()
