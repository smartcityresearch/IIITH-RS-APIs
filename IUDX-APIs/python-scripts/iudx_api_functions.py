import requests
import json


def get_token(auth_server_url, clientId, clinetSecret, itemId, itemType, data_format="json"):
    """
        Method description:
        A POST request to get the token from IUDX Authoriation Server

        Parameters:
        auth_server_url : [str] URL of the IUDX authorization server,
        clientId : [str] IUDX client ID (UUID),
        clientSecret : [str] IUDX client secret/password (40 chars in hexadecimal),
        itemId : [str] item ID Ex. Resource Server domain name(for open resource) / Resource Group ID (for secure resource),
        itemType : [str] resource_server (for open resource) / resource_group (for secure resource)
    """
    headers = {
        'clientId': clientId,
        'clientSecret': clinetSecret
        }

    body = {
        "itemId": itemId,
        "itemType": itemType,
        "role": "consumer"
        }
    try:
        try:
            response = requests.post(auth_server_url + "/auth/v1/token", json=body, headers=headers)
        except TypeError:
            response = requests.post(auth_server_url + "/auth/v1/token", data=json.dumps(body), headers=headers)
        return  json.loads(response.text)["results"]["accessToken"]
    except:
        return response.status_code, json.dumps(response.json(), indent = 2)


def get_version_info(resource_server_url, resource_group_id, token, deviceID = "nan", data_format="json"):
    """
        Method description:
        A POST request to get the token from IUDX Authoriation Server

        Parameters:
        resource_server_url : [str] URL of the resource,
        token : [str] token received from IUDX authorization server,
        resource_group_id : [str] ID of the group resource whose version information needs to be retrieved
        deviceID : [str] ID of the IIITH node whose version information needs to be retrieved
    """
    headers = {
        'token': token,
              }
    if deviceID == "nan":
        response = requests.get(resource_server_url + "/ngsi-ld/v1/entities?id=" + resource_group_id, headers=headers)
    else:
        response = requests.get(resource_server_url + "/ngsi-ld/v1/entities?id=" + resource_group_id + "&" + \
                                "q="+ '"' + "deviceInfo.deviceID==" + deviceID + '"', headers=headers)
    return response.status_code, json.dumps(response.json() , indent=2)


def get_latest_data(resource_server_url, resource_id, token, data_format="json"):
    """
        Method description:
        A POST request to get the token from IUDX Authoriation Server

        Parameters:
        resource_server_url : [str] URL of the resource,
        token : [str] token received from IUDX authorization server,
        resource_id : [str] ID of the resource whose version information needs to be retrieved
    """
    headers = {
        'token': token,
              }

    response = requests.get(resource_server_url +  "/ngsi-ld/v1/entities/" + resource_id, headers=headers)
    return response.status_code, json.dumps(response.json() , indent=2)

def get_temporal_data(resource_server_url, resource_id, token, timerel = "nan", time = "nan", endtime = "nan", \
                      attrs = "nan", options = "nan", limit = str(2000), offset = str(0), data_format="json"):
    """
        Method description:
        A POST request to get the token from IUDX Authoriation Server

        Parameters:
        resource_server_url : [str] URL of the resource server,
        resource_id : [str] ID of the resource whose version information needs to be retrieved,
        token : [str] token received from IUDX authorization server,
        timerel = [str] The time relation of the query. Should be either during, before or after,
        time = [str] Start time for the temporal query in ISO 8601 format,
        endtime = [str] End time for the temporal query in ISO 8601 format. Applicable only for timerel = during,
        options = [str] The value should be equal to count and it is case sensitive,
        limit = [str] The size parameter allows you to configure the maximum results to be returned
                        ( default: 2000 ,minValue: 0, maxValue: 2000 (for IIIT-H Resource Server) ),
        offset = [str] The from parameter defines the offset from the first result you want to fetch, 
                        ( default : 0 ,minValue: 0, maxValue: 49999 ),
        Note:   The time difference between time and endtime should be less than 10 days. For before and after queries, 
                10 days of data before or after the specified time will be provided.

    """
    headers = {
        'token': token,
              }

    if timerel == "after" or timerel == "before":
        if options == "nan":
            response = requests.get(resource_server_url + "/ngsi-ld/v1/temporal/entities?id=" + resource_id + "&" + \
                            "timerel=" + timerel + "&" + "time=" + time + "&" + "attrs=" + attrs + "&" +  "limit=" + \
                            limit + "&" + "offset=" + offset, headers=headers)
        else:
            response = requests.get(resource_server_url + "/ngsi-ld/v1/temporal/entities?id=" + resource_id + "&" + \
                            "timerel=" + timerel + "&" + "time=" + time + "&" + "attrs=" + attrs + "&" +  "limit=" + \
                            limit + "&" + "offset=" + offset, headers=headers)
    elif timerel == "during":
        if options == "nan":
            response = requests.get(resource_server_url + "/ngsi-ld/v1/temporal/entities?id=" + resource_id + "&" + \
                            "timerel=" + timerel + "&" + "time=" + time + "&" + "endtime=" + endtime  + "&" + "attrs=" \
                            + attrs + "&" + "limit=" + limit + "&" + "offset=" + offset, headers=headers)
        else:
            response = requests.get(resource_server_url + "/ngsi-ld/v1/temporal/entities?id=" + resource_id + "timerel=" \
                            + timerel + "&" + "time=" + time + "&" + "attrs=" + attrs + "&" + "options=" + options + \
                             "limit=" + limit + "&" + "offset=" + offset, headers=headers)
    else:
        response = requests.get(resource_server_url + "/ngsi-ld/v1/temporal/entities?id=" + resource_id + "timerel=" \
                            + timerel + "&" + "time=" + time + "&" + "attrs=" + attrs + "&" + "options=" + options + \
                             limit + "&" + offset, headers=headers)
    return response.status_code, json.dumps(response.json() , indent=2)

# =====================================================================================

if __name__ == "__main__":
    auth_server_url = "https://authvertx.iudx.io"

