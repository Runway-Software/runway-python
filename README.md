# Runway Python SDK
This is a python library used for connecting to the Runway REST API. The documentation for this api can be found at:
https://portal.runway.host/api/docs/index.html?url=/swagger/v1/swagger.json

# Installing the package
```
git clone https://github.com/pjv4yj/runway-sdk.git
cd runway-sdk
pip3 install -e .
```

# Authenticating with the SDK
To authenticate to the api, run the following commands in your terminal from the runway-sdk directory:
```
cd examples
python3 authentication_example.py
```
This will print a session token to the console. Do the following with the session token:
```
export RUNWAY_SESSION_ID=<SESSION ID>
```
You will then be able to make any call using the Runway SDK

# Sample API Call
This sample call gets a list of all endpoint assets in the Runway instance

```
endpoint_assets_result = runway_obj.endpoint_asset.list(headers=headers)
print(endpoint_assets_result)
```

# Documentation
We are currently working on providing more documentation and sample API calls using the SDK. In the meantime, please see the examples directory found under python-sdk for authentication, user, endpoint, and job example functions. The example folder is found [here](./examples)

# Info
- Modifiable: yes
- Generated: all
- Committed: yes
- Packaged: yes

# Detail
This module was primarily generated via [AutoRest](https://github.com/Azure/autorest) using the [Python](https://github.com/Azure/autorest.python) extension.
