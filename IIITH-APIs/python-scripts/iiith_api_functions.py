"""
	The code contains functions required to retrieve data from IIITH Resource Server (Version 1.0.0) using IIITH-APIs.

	Initial Contributors:
        Shubham Mante : Master Research Scholar, IIIT-Hyderabad, India
	Suhas Vaddhiparthy: Master Research Scholar, IIIT-Hyderabad, India
   
    New contributors :
"""


import requests
import json


def get_api_key(user_email, user_pass, data_format="json"):
    """
        Method description:
        A POST request to get the api_key

        Parameters:
        user_email : [str] A valid IIIT-H email ID that is previously used during user registration,
        user_pass : [str] Password that is previously used during user registration 
    """
    body = {
        "email": user_email,
        "password": user_pass
        }
    try:
        response = requests.post("https://iudx-rs-onem2m.iiit.ac.in/api/get-api_key", json=body)
    except TypeError:
        response = requests.post("https://iudx-rs-onem2m.iiit.ac.in/api/get-api_key", data=json.dumps(body))
    return  json.loads(response.text)["results"]["accessApiKey"]

def introspect_api_key(api_key, data_format="json"):
    """
        Method description:
        A POST request to introspect the api_key

        Parameters:
        api_key : [str] api_key that is obtained by providing valid credentials,
    """
    body = {
        "api_key": api_key
        }
    try:
        response = requests.post("https://iudx-rs-onem2m.iiit.ac.in/api/introspect", json=body)
    except TypeError:
        response = requests.post("https://iudx-rs-onem2m.iiit.ac.in/api/introspect", data=json.dumps(body))
    print("Result Content:",response.text)
    return  response.status_code, json.dumps(response.json(), indent=2)

def get_latest_data(api_key, device_id, data_format="json"):
    """
        Method description:
        A GET request to get the latest data of given iot node

        Parameters:
        api_key : [str] api_key that is obtained by providing valid credentials
    """

    response = requests.get("https://iudx-rs-onem2m.iiit.ac.in/channels/" + device_id + "/feeds/last.json?api_key=" + api_key)
    return response.status_code, json.dumps(response.json() , indent=2)

def get_temporal_data(api_key, node_id, start_time = None, end_time = None, data_format="json"):
    """
        Method description:
        A GET request to get the temporal data of given IoT node

        Parameters:
        api_key : [str] api_key that is obtained by providing valid credentials,
        node_id : [str] ID of the node as per oneM2M resource tree,
        start_time : [str] Start time for the temporal query in [YYYY-MM-DD  HH:MM:SS] format,
        end_time : [str] Start time for the temporal query in [YYYY-MM-DD  HH:MM:SS] format,

    """
    if start == None:
        response = requests.get("https://iudx-rs-onem2m.iiit.ac.in/channels/" + node_id + "/feeds.json?api_key=" + \
                                api_key + "end=" + end_time)
    elif end == None:
        response = requests.get("https://iudx-rs-onem2m.iiit.ac.in/channels/" + node_id + "/feeds.json?api_key=" + \
                                api_key + "start=" + start_time)
    elif start ==None and end == None:
        response = requests.get("https://iudx-rs-onem2m.iiit.ac.in/channels/" + node_id + "/feeds.json?api_key=" + \
                                api_key)
    elif start !=None and end != None:
        response = requests.get("https://iudx-rs-onem2m.iiit.ac.in/channels/" + node_id + "/feeds.json?api_key=" + \
                                api_key + "start=" + start_time + "end=" + end_time)
    else:
        response = ""
        print("Incorrect URL endpoint")
    return json.dumps(response.json() , indent=2)

# =====================================================================================

if __name__ == "__main__":
    iiith_rs_url = "https://iudx-rs-onem2m.iiit.ac.in"

