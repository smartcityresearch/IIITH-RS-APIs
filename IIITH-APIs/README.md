# IIITH-RS-IIITH-APIs* 
It is assumed that you have already imported the IIITH-RS-IIITH-APIs.postman_collection.json & IIITH-RS_IIITH_Environment.postman_environment.json files in POSTMAN prior to the procedure given below.

# User Registration Procedure
* ***Step-1:*** Enter the username, email ID (iiit domain: @iiit.ac.in, @research.iiit.ac.in, @ students.iiit.ac.in) and password (store the password for future usage)

![register_user.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IIITH-APIs/images/register_user.png)
* ***Step-2:*** You will receive a One Time Password (OTP) on the email that you have used during user registration (Check the spam/junk folder if you didn't receive the email in Inbox folder). Use this OTP for user confirmation step.

![confirm_user.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IIITH-APIs/images/confirm_user.png)
* In this way, a IIITH consumer can create the profile.

# Get Token for data retrieval
* ***Step-1:*** Enter the valid email ID & password in the body of the GET api_key POST request. (You can use the python script too)

![get_api_key.png](https://github.com/smartcityresearch/IIITH-RS-APIs/blob/main/IIITH-APIs/images/get_api_key.png)
* ***Step-2:*** Click on the send button to get the api_key.
* ***Step-3:*** Use the token to get the latest / temporal data

