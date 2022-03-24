import runway.sdk.models as models
from runway.sdk import PyRunway

# Basic setup to connect to Runway REST API
runway_obj = PyRunway(email="pjv4yj@virginia.edu", password="Kali@0921")
print(runway_obj.headers)

