import pytest
import requests
import json

url = 'http://127.0.0.1:5000' # The root url of the flask app

def test_get_partners(self):

    response = requests.get(url+'/partners')
    assert response.status_code == 200

def test_get_partner(self):
    response = requests.get(url+'/partners/1')
    assert response.status_code == 200
    
def test_create_partner(self):

    json_partner = {
        "id": "100",
        "tradingName": "Adega da Cerveja - Pinheiros",
        "ownerName": "Zé da Silva",
        "document": "1432132123891/0001",
        "coverageArea": { 
        "type": "MultiPolygon", 
        "coordinates": [
            [[[30, 20], [45, 40], [10, 40], [30, 20]]], 
            [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
        ]
        },
        "address": { 
        "type": "Point",
        "coordinates": [-46.57421, -21.785741]
        }
    }

    response = requests.post(url+'/partners/', headers={"Content-Type": "application/json"}, data=json.dumps(json_partner))
    assert response.status_code == 201