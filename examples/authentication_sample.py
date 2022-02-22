import runway.sdk.models as models
from runway.sdk import PyRunway

# Basic setup to connect to Runway REST API
runway_obj = PyRunway()
login_request = models.LoginRequest(remember=True,email="<email address>",password="<password>")
authentication_result = runway_obj.authentication.login(request=login_request)
session_id = authentication_result.session
headers = {"Authorization" : "Session " + session_id}

print(headers)
