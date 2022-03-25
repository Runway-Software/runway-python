import runway.sdk.models as models
from runway.sdk import PyRunway

# Basic setup to connect to Runway REST API
runway_obj = PyRunway(email="<email address>", password="<password>")
print(runway_obj.headers)
