from iudx_api_functions import *
import requests
import json
import os

#================================== DECLARE VARIABLES ==============================================================================

resource_server_url = "https://iudx-rs-onem2m.iiit.ac.in/"
auth_server_url = "https://authvertx.iudx.io"
clinetId = "3256f877-2e28-418a-8db3-abfbe1e79dae"
clinetSecret = "b890b0dc55bd68cbf5323cbe5988985f3b104d3d"
open_itemId = "iudx-rs-onem2m.iiit.ac.in"
open_itemType = "resource_server"
aqm_version_id = "research.iiit.ac.in/4786f10afbf48ed5c8c7be9b4d38b33ca16c1d9a/iudx-rs-onem2m.iiit.ac.in/iiith-env-aqm-version/version-info"
deviceID = "AQ-MG00-00"
aqm_resource_id = "research.iiit.ac.in/4786f10afbf48ed5c8c7be9b4d38b33ca16c1d9a/iudx-rs-onem2m.iiit.ac.in/iiith-env-aqm/AQ-AN00-00"

#================================= TO GET VERSION ==============================================================================

if os.getenv('iiith_rs_open_resource_token') == None:
    os.environ['iiith_rs_open_resource_token'] = get_token(auth_server_url, clinetId, clinetSecret, open_itemId, open_itemType)
else:
    status_code, version_info = get_version_info(resource_server_url, aqm_version_id, os.getenv('iiith_rs_open_resource_token'))
    if status_code == 401:
        os.environ['iiith_rs_open_resource_token'] = get_token(auth_server_url, clinetId, clinetSecret, open_itemId, itemType)
    else:
        pass

#================================== TO GET VERSION INFORMATION ==================================================================

# status_code, version_info = get_version_info(resource_server_url, aqm_version_id, os.getenv('iiith_rs_open_resource_token'))
# print(version_info)

# status_code, version_info = get_version_info(resource_server_url, aqm_version_id, os.getenv('iiith_rs_open_resource_token'), deviceID)
# print(version_info)

#================================== TO GET LATEST DATA ==========================================================================

# status_code, latest_data = get_latest_data(resource_server_url, aqm_resource_id, os.getenv('iiith_rs_open_resource_token'))
# print(latest_data)

#================================== TO GET TEMPORAL DATA ==========================================================================
"""
    options = [str] The value should be equal to count and it is case sensitive {optional}

"""

# status_code, temporal_data_after = get_temporal_data(resource_server_url, aqm_resource_id, os.getenv('iiith_rs_open_resource_token'), timerel = "after", time = "2021-08-20T15:30:00Z")
# print(temporal_data_after)

# status_code, temporal_data_before = get_temporal_data(resource_server_url, aqm_resource_id, os.getenv('iiith_rs_open_resource_token'), timerel = "before", time = "2021-08-20T15:30:00Z")
# print(temporal_data_before)

# status_code, temporal_data_during = get_temporal_data(resource_server_url, aqm_resource_id, os.getenv('iiith_rs_open_resource_token'), timerel = "during", time = "2021-08-20T15:30:00Z", endtime = "2021-08-21T15:30:00Z")
# print(temporal_data_during)

