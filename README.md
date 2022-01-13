# IIITH-RS-APIs

# POSTMAN
* Download and install the POSTMAN REST client: http://www.postman.com

# POSTMAN_collection 
* The postman collections are inside "***postman-collections***" folder:
    1. IIITH-APIs --> postman-collections 
    2. IUDX-APIs --> postman-collections
* Import the collections (APIs & Environment) ( in POSTMAN as explained in: https://apitransform.com/how-to-import-a-collection-into-postman/
* Create the user profile and then get information ( version, data) using obtained token (IUDX_APIs) / api_key (IIITH_APIs)


# python_codes
* Install the "requests", "os" and "json" modules (skip this step if already installed)
* Uncomment required code lines and run get_data script (iiith_api_get_data.py / iudx_api_get_data) to get token / api_key and data (Latest and Temporal)


***Note:*** The user registration process for IUDX_APIs and IITH_APIs should be done only once so it is recommended to complete it using Postman Collection. Later, you can use Python scripts.
