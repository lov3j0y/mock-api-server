import json
import os
import pytest
from dotenv import load_dotenv
import requests


CA_BUNDLE = os.getenv("REQUESTS_CA_BUNDLE")

def load_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def get_default_data_filepath():
    host = os.getenv("HOST", "localhost")
    
    if host == "localhost":
        INVENTORY_DEVICES_FILE = 'app/responses/inventory_devices.json'
        GUIDS_FILE = 'app/responses/guids.json'
    else:
        INVENTORY_DEVICES_FILE = '/opt/project/app/responses/inventory_devices.json'
        GUIDS_FILE = '/opt/project/app/responses/guids.json'
        
    return INVENTORY_DEVICES_FILE, GUIDS_FILE

INVENTORY_DEVICES_FILE = get_default_data_filepath()[0]
GUIDS_FILE = get_default_data_filepath()[1]

default_inventory_devices_response = load_json_file(INVENTORY_DEVICES_FILE)
default_guids_response = load_json_file(GUIDS_FILE)


def get_base_url():
    protocol = os.getenv("PROTOCOL", "http")  # Defaults to 'http' if not set
    host = os.getenv("HOST", "localhost")  # Defaults to 'localhost' if not set
    port = os.getenv("PORT", "8080")  # Defaults to '8080' if not set
    
    if protocol == "https":
        base_url = os.getenv(f"BASE_URL_{host.upper()}_HTTPS", f"https://{host}:{port}")
    else:
        base_url = os.getenv(f"BASE_URL_{host.upper()}_HTTP", f"http://{host}:{port}")

    return base_url

BASE_URL = get_base_url()

@pytest.fixture(autouse=True)
def reset_mock_data():
    """
    Reset the current state to the initial state.
    """
    #Make sure the mock data is in default state before the test.
    print("Resetting mock data...")
    requests.put(f"{BASE_URL}/inventory/devices", json=default_inventory_devices_response, verify=CA_BUNDLE)
    requests.put(f"{BASE_URL}/guids", json=default_guids_response, verify=CA_BUNDLE)

    yield
    
    # Reset mock data after the test
    requests.put(f"{BASE_URL}/inventory/devices", json=default_inventory_devices_response, verify=CA_BUNDLE)
    requests.put(f"{BASE_URL}/guids", json=default_guids_response, verify=CA_BUNDLE)