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
This sample code generates a headers variable which should be passed to each endpoint function (check the examples folder for more clarity)

```
import runway.sdk.models as models
from runway.sdk import PyRunway

runway_obj = PyRunway()
login_request = models.LoginRequest(remember=True,email="<email address>",password="<password>")
authentication_result = runway_obj.authentication.login(request=login_request)
session_id = authentication_result.session
headers = {"Authorization" : "Session " + session_id}
```

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
