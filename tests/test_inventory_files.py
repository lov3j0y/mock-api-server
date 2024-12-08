import os
import requests
from conftest import *


def test_get_root_ca_cert():
    url = f"{BASE_URL}/mock_certs/root_ca"
    response = requests.get(url, verify=CA_BUNDLE)
    assert response.status_code == 200
    assert "-----BEGIN CERTIFICATE-----" in response.text
    assert "-----END CERTIFICATE-----" in response.text


def test_get_intermediate_ca_cert():
    url = f"{BASE_URL}/mock_certs/intermediate_ca"
    response = requests.get(url, verify=CA_BUNDLE)
    assert response.status_code == 200
    assert "-----BEGIN CERTIFICATE-----" in response.text
    assert "-----END CERTIFICATE-----" in response.text


def test_post_image_add_success():
    url = f"{BASE_URL}/file/add"
    test_file_path = '/tmp/test_image.jpg'    
    
    with open(test_file_path, 'wb') as f:
        f.write(b'Test content')

    with open(test_file_path, 'rb') as test_file:
        response = requests.post(url, files={'file': ('test_image.jpg', test_file)}, verify=CA_BUNDLE)

    assert response.status_code == 200
    assert "File uploaded successfully" in response.text
    
    os.remove(test_file_path)


def test_post_image_add_no_file():
    url = f"{BASE_URL}/file/add"
    response = requests.post(url, verify=CA_BUNDLE)
    assert response.status_code == 400
    assert response.text == "No file part in the request"


def test_post_image_add_no_selected_file():
    url = f"{BASE_URL}/file/add"
    response = requests.post(url, files={'file': ('', '')}, verify=CA_BUNDLE)
    assert response.status_code == 400
    assert response.text == "No selected file"
