"""
	The code contains a method to retrieve data from IIITH Resource Server (Version 1.0.0) using IUDX-APIs.

	Initial Contributors:
        Shubham Mante : Master Research Scholar, IIIT-Hyderabad, India
	Suhas Vaddhiparthy: Master Research Scholar, IIIT-Hyderabad, India
   
    New contributors :
"""

from iudx_api_functions import *
import requests
import json
import os

#================================== DECLARE VARIABLES ==============================================================================

resource_server_url = "https://iudx-rs-onem2m.iiit.ac.in/"
auth_server_url = "https://authvertx.iudx.io"
clinetId = os.getenv('shubham_iudx_clientId')
clinetSecret = os.getenv('shubham_iudx_clientSecret')
open_itemId = "iudx-rs-onem2m.iiit.ac.in"
open_itemType = "resource_server"
aqm_version_id = "research.iiit.ac.in/4786f10afbf48ed5c8c7be9b4d38b33ca16c1d9a/iudx-rs-onem2m.iiit.ac.in/iiith-env-aqm-version/version-info"
deviceID = "AQ-AN00-00"
aqm_resource_id = "research.iiit.ac.in/4786f10afbf48ed5c8c7be9b4d38b33ca16c1d9a/iudx-rs-onem2m.iiit.ac.in/iiith-env-aqm/AQ-MG00-00"

#================================= TO GET TOKEN ==============================================================================

try:
    with open("rs.token", "r") as file:
        token = file.read()
        print(" Current token:", token)
except Exception as file_exception:
    with open("rs.token", "w") as file:
        token = get_token(auth_server_url, clinetId, clinetSecret, open_itemId, open_itemType)
        file.write(str(token))

status_code, introspect_result = introspect_token(auth_server_url, token)
print("\n Token status code:", status_code)
if status_code == 401:
    try:
        with open("rs.token", "w") as file:
            token = get_token(auth_server_url, clientId, clientSecret, open_itemId, open_itemType)
            file.write(str(token))
    except Exception as token_expired:
        pass
else:
    pass

#================================== TO GET VERSION INFORMATION ==================================================================

# status_code, version_info = get_version_info(resource_server_url, aqm_version_id, token)
# print("\n Group version information:" + version_info)

# status_code, version_info = get_version_info(resource_server_url, aqm_version_id, token, deviceID)
# print("\n Version of " + deviceID + ":" + version_info)

#================================== TO GET LATEST DATA ==========================================================================

status_code, latest_data = get_latest_data(resource_server_url, aqm_resource_id, token)
print("\n Latest data of " + aqm_resource_id + ":" + latest_data)

#================================== TO GET TEMPORAL DATA ==========================================================================
"""
    options = [str] The value should be equal to count and it is case sensitive {optional}

"""

# status_code, temporal_data_after = get_temporal_data(resource_server_url, aqm_resource_id, token, timerel = "after", time = "2021-08-20T15:30:00Z")
# print("\n Temporal data of " + aqm_resource_id + ":" + temporal_data_after)

# status_code, temporal_data_before = get_temporal_data(resource_server_url, aqm_resource_id, token, timerel = "before", time = "2021-08-20T15:30:00Z")
# print("\n Temporal data of " + aqm_resource_id + ":" + temporal_data_before)

# status_code, temporal_data_during = get_temporal_data(resource_server_url, aqm_resource_id, token, timerel = "during", time = "2021-08-20T15:30:00Z", endtime = "2021-08-21T15:30:00Z")
# print("\n Temporal data of " + aqm_resource_id + ":" + temporal_data_during)

