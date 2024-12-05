# Test Cases for Inventory of Devices API

---

## Test Case 1: Retrieve All Devices

- **Test Case ID**: TC_INV_001  
- **Title**: Verify the API returns the list of inventory devices.  
- **Pre-conditions**:  
  - The API is running and accessible at `/inventory/devices`.  
  - At least one device is available in the inventory.  
- **Test Steps**:  
  1. Send a `GET` request to `/inventory/devices`.  
  2. Validate the response status code.  
  3. Check that the response body contains a list of devices.  
  4. Verify that each device in the list contains required fields (e.g., `id`, `ipAddress`, `model`).  
- **Expected Result**:  
  - Status code: `200 OK`.  
  - The response contains a list of devices, each having all the required fields.  
- **Actual Result**: Actual result is as expected.  
- **Status**: Pass
- **Notes**: None

---

## Test Case 2: Retrieve All GUIDs

- **Test Case ID**: TC_INV_002  
- **Title**: Verify the API handles empty GUID lists gracefully.  
- **Pre-conditions**:  
  - The API is running and accessible at `/guids`.  
  - The `guid` list is empty.  
- **Test Steps**:  
  1. Send a `GET` request to `/guids`.  
  2. Validate the response status code.  
  3. Check that the response contains an empty `guid` list.  
- **Expected Result**:  
  - Status code: `200 OK`.  
  - The response contains an empty list for `guid`.  
- **Actual Result**: Actual result is as expected. 
- **Status**: Pass 
- **Notes**: None

---

## Test Case 3: Add a New GUID

- **Test Case ID**: TC_INV_003  
- **Title**: Verify the API allows adding a new GUID.  
- **Pre-conditions**:  
  - The API is running and accessible at `/guids`.  
  - The GUID to be added does not already exist.  
- **Test Steps**:  
  1. Send a `POST` request to `/<guid>/add` with a valid GUID.  
  2. Validate the response status code.  
  3. Check that the response contains the added GUID in the `guid` list.  
- **Expected Result**:  
  - Status code: `200 OK`.  
  - The response contains the newly added GUID in the list.  
- **Actual Result**: Actual result is as expected.  
- **Status**: Pass 
- **Notes**: None    

---

## Test Case 4: Update Device List with Valid Data

- **Test Case ID**: TC_INV_004  
- **Title**: Verify the API accepts valid data for updating the device list.  
- **Pre-conditions**:  
  - The API is running and accessible at `/inventory/devices`.  
- **Test Steps**:  
  1. Send a `PUT` request to `/inventory/devices` with a valid payload. 
  2. Validate the response status code.  
  3. Check that the response body contains a list of devices with updated data.    
- **Expected Result**:  
  - Status code: `200 OK`.  
  - The response contains a list of devices with updated data.  
- **Actual Result**:
  - Status code: `200 OK` 
- **Status**: Pass
- **Notes**: None  

---

## Test Case 5: Update Device List with Invalid Data

- **Test Case ID**: TC_INV_005  
- **Title**: Verify the API rejects invalid data for updating the device list.  
- **Pre-conditions**:  
  - The API is running and accessible at `/inventory/devices`.  
- **Test Steps**:  
  1. Send a `PUT` request to `/inventory/devices` with an invalid payload (e.g., missing required fields like `id`, `model`).  
  2. Validate the response status code.  
  3. Check the error message in the response body.  
- **Expected Result**:  
  - Status code: `400 Bad Request`.  
  - The response contains an appropriate error message indicating invalid data.  
- **Actual Result**:
  - Status code: `200 OK`. The system allows user to updated with invalid data.  
- **Status**: Fail
- **Notes**: There is bug here, because the app returns wrong status code and allows the user to update data with missing fields.  

---
## Test Case 6: Add Duplicate GUID

- **Test Case ID**: TC_INV_006  
- **Title**: Verify the API behavior when attempting to add a duplicate GUID.  
- **Pre-conditions**:  
  - The API is running and accessible at `/guids`.  
  - The GUID to be added already exists in the list.  
- **Test Steps**:  
  1. Send a `POST` request to `/<guid>/add` with a duplicate GUID.  
  2. Validate the response status code.  
  3. Check if the API allows the duplicate or returns an error.  
- **Expected Result**:  
  - Status code: `400 Bad Request` (if duplicates are not allowed).  
  - Alternatively, status code: `200 OK` with no changes to the `guid` list (if duplicates are allowed).  
- **Actual Result**: Duplicated guid is added to the `guid` list, the status code is 200. 
- **Status**: Pass. 
- **Notes**: API behavior for duplicates needs to be clarified. My common sense makes me consider this as a bug, because guid should be unique, but this is not stated explicitly in the documentation.  
