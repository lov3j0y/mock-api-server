import requests
import pytest
from conftest import *


def test_get_inventory_devices(verify=CA_BUNDLE):
    """
    Test GET /inventory/devices endpoint to retrieve all devices.
    """
    response = requests.get(f"{BASE_URL}/inventory/devices")
    assert response.status_code == 200
    assert response.json() == default_inventory_devices_response['body']


def test_update_inventory_devices_with_valid_data(verify=CA_BUNDLE):
    """
    Test PUT /inventory/devices endpoint to update the devices response.
    """
    updated_data ={
        "body": [
            {
            "id": "UPDATED_TEST1",
            "ipAddress": "10.0.49.140",
            "deviceAddresses": {
                "fqdn": "updated.com",
                "ipv4Address": "192.168.0.1",
                "ipv6Address": None
            },
            "model": "UPDATED_TEST_DEVICE",
            "serialNum": "UPDATED_TEST1-1fecaf6a-0619-41b1-86d8-acf36064f9ec",
            "version": "2.3.12",
            "build": "20240410.1854-8f4e21frg65t"
            },
            {
            "id": "TEST2",
            "ipAddress": "10.0.49.141",
            "deviceAddresses": {
                "fqdn": "test.com",
                "ipv4Address": "10.0.49.141",
                "ipv6Address": "2de4:712b:d13d:d51e:0d5f:3530:1d51:1493"
            },
            "model": "TEST_DEVICE",
            "serialNum": "TEST2-1ghfaf6a-0723-52e1-86d8-acf42055f9eg",
            "version": "3.0.0",
            "build": "20240410.1854-8f4e21y111ef-snapshot"
            }
        ],
        "status_code": 200
    }
    response = requests.put(f"{BASE_URL}/inventory/devices", json=updated_data)
    assert response.status_code == 200
    assert response.json()["new_body"] == updated_data["body"]
    assert response.json()["new_status_code"] == updated_data["status_code"]
    
def test_update_inventory_devices_with_invalid_data(verify=CA_BUNDLE):
    """
    Test PUT /inventory/devices endpoint to update the devices response.
    """
    updated_data = {
        "body": [
            {
                "id": "UPDATED_DEVICE",
                "ipAddress": "192.168.0.1",
                "deviceAddresses": {
                    "fqdn": "updated.com",
                    "ipv4Address": "192.168.0.1",
                    "ipv6Address": "abcd:ef01:2345:6789:abcd:ef01:2345:6789"
                },               
            }
        ],
        "status_code": 400
    }
    response = requests.put(f"{BASE_URL}/inventory/devices", json=updated_data)
    assert response.status_code == 400

def test_get_guids(verify=CA_BUNDLE):
    """
    Test GET /guids endpoint to retrieve all GUIDs.
    """     
    response = requests.get(f"{BASE_URL}/guids")
    expected_response = default_guids_response["body"]
    assert response.status_code == 200
    assert response.json() == expected_response

def test_post_guid_add(verify=CA_BUNDLE):
    """
    Test POST /<guid>/add endpoint to add a new GUID.
    """
    guid = "123e4567-e89b-12d3-a456-426614174000"
    response = requests.post(f"{BASE_URL}/{guid}/add")
    assert response.status_code == 200
    guid_add_response = {
        "body": {
            "guids": [guid]
        },
        "status_code": 200
    }
    assert response.json() == guid_add_response["body"]
    
def test_post_guid_add_duplicated_value(verify=CA_BUNDLE):
    """
    Test POST /<guid>/add endpoint to add a duplicated GUID.
    """
    guid = "123e4567-e89b-12d3-a456-426614174000"
    get_all_guids = requests.get(f"{BASE_URL}/guids")
    assert get_all_guids.json() == default_guids_response["body"]
    assert get_all_guids.status_code == 200
    requests.post(f"{BASE_URL}/{guid}/add") 
    requests.post(f"{BASE_URL}/{guid}/add")
    duplicated_response = {
        "body": {
            "guids": [guid, guid]
        },
        "status_code": 200
    }
    current_all_guids = requests.get(f"{BASE_URL}/guids")
    assert current_all_guids.json() == duplicated_response["body"]
    assert current_all_guids.status_code == 200

