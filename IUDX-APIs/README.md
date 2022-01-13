# IIITH-RS-IUDX-APIs
* It is assumed that you have already imported the IIITH-RS-IUDX-APIs.postman_collection.json & IIITH-RS_IUDX_Environment.postman_environment.json files in POSTMAN prior to the procedure given below.

# User Registration Procedure
* As the auth server uses OIDC token-based authentication, an OIDC JWT token is required to be sent along with most requests. Postman eases the process of obtaining said tokens by providing the Authorization tab in each request. The details needed to configure getting tokens have already been filled out. 

* ***Step-1:*** Click the ***Get New Access Token*** button under authorization (Auth) tab, after which you will be prompted to enter the email address and password.

![keycloak_get_new_token.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IUDX-APIs/images/keycloak_get_new_token.png)

![keycloak_registration_window.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IUDX-APIs/images/keycloak_registration_window.png)
* ***Step-2:*** Click on ***Register***,  fill the required information and click on ***Register*** and close the window.

![keycloak_user_registration.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IUDX-APIs/images/keycloak_user_registration.png)
* ***Step-3:*** You will receive a link on the email that you have used during user registration (Check the spam/junk folder if you didn't receive the email in Inbox folder). Click on the link and activate your keycloak account.
* ***Step-4:*** Click the ***Get New Access Token*** button, after which you will be prompted to enter the email address and password you have registered with. If the credentials are correct, a token is returned. Click Use Token to use that particular token while sending a request to resource server.
* ***Step-5:*** Send the POST request along with the token obtained during ***Step-4:***  (The required details are already filled in the body of the Create User Profile POST request as shown below.)

![create_user_profile.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IUDX-APIs/images/create_user_profile.png)
* Please save the response that you will received after ***Step-5*** into a separate file for future reference ***(Don't Lose the clientId & clientSecret)***. The clientId and client Secret will be needed to get the tokens. 
* In this way, a consumer can create the profile for a particular organization (IIITH organization Id: ***c42709ce-1565-450a-9257-3c0739420ef8***)

# Get Token for Open Resources (iiith-env-aqm & iiith-env-weather)
* ***Step-1:*** Enter the valid clientId & clientSecret in the headers of Get token API request in POSTMAN collection. (You can use the python script too)
* ***Step-2:*** Click on the send button to get the token for open resource. The body of default Get token API request of POSTMAN collection contains the information to get token for open resource.

![open_resource_get_token.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IUDX-APIs/images/open_resource_get_token.png)
* ***Step-3:*** Use the token to get the version information/ latest data/ temporal data

# Get Token for Secure Resources (iiith-energy-meter & iiith-water-monitoring)
* ***Step-0:*** Ask the data provider to give you (consumer) the access to use APIs (version/latest/temporal) of secure resources.
* ***Step-1:*** Enter the valid clientId & clientSecret in the headers
* ***Step-2:*** Click on the send button to get the token for open resource. Change the body of the POST request by adding the resource ID for which you need the token. The itemType will be resource_group as shown below.

![secure_resource_get_token.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IUDX-APIs/images/secure_resource_get_token.png)
* ***Step-3:*** Use the token to get the version information/ latest data/ temporal data

# Reference:
* https://rs.iudx.org.in/apis
* https://api.catalogue.iudx.org.in/apis
* https://github.com/datakaveri/

