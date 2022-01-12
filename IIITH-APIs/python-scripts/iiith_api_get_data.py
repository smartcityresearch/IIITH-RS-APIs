from iiith_api_functions import *
import requests
import json
import os

#================================== DECLARE VARIABLES ==============================================================================

user_email = os.getenv('shubham_iiith_rs_email')
user_password = os.getenv('shubham_iiith_rs_password')
device_id = "AQ-AN00-00"

#================================= TO GET api_key ==============================================================================

try:
    with open("rs.api_key", "r") as file:
        api_key = file.read()
        print(" Current api_key:", api_key)
except Exception as file_exception:
    with open("rs.api_key", "w") as file:
        api_key = get_api_key(user_email, user_password)
        file.write(str(api_key))

status_code, introspect_result = introspect_api_key(api_key)
print("\n api_key status code:", status_code)
if status_code == 401:
    try:
        with open("rs.api_key", "w") as file:
            api_key = get_api_key(user_email, user_password)
            file.write(str(api_key))
    except Exception as api_key_expired:
        pass
else:
    pass

#================================== TO GET LATEST DATA ==========================================================================

status_code, latest_data = get_latest_data(api_key, device_id)
print("\n Latest data of " + device_id + ":" + latest_data)

#================================== TO GET TEMPORAL DATA ==========================================================================
"""
    options = [str] The value should be equal to count and it is case sensitive {optional}

"""

# status_code, temporal_data_start = get_temporal_data(api_key, device_id, start = "2021-08-20T15:30:00Z")
# print("\n Temporal data of " + device_id + ":" +temporal_data_start)

# status_code, temporal_data_end = get_temporal_data(api_key, device_id, end = "2021-08-20T15:30:00Z")
# print("\n Temporal data of " + device_id + ":" +temporal_data_end)

# status_code, temporal_data_start-end = get_temporal_data(api_key, device_id, start = "2021-08-20T15:30:00Z", end = "2021-08-21T15:30:00Z")
# print("\n Temporal data of " + device_id + ":" +temporal_data_start_end)

