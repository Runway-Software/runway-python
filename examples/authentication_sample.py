import runway.sdk.models as models
from runway.sdk import PyRunway

# Basic setup to connect to Runway REST API
runway_obj = PyRunway()
print(runway_obj.getHeaders(email="<email address>", password="<password>"))
