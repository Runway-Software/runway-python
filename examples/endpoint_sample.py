import runway.sdk.models as models
from runway.sdk import PyRunway

# Basic setup to connect to Runway REST API
runway_obj = PyRunway()
login_request = models.LoginRequest(remember=True,email="<email address>",password="<password>")
authentication_result = runway_obj.authentication.login(request=login_request)
session_id = authentication_result.session
headers = {"Authorization" : "Session " + session_id}

"""
Example calls for these endpoint functions
get_all_endpoint_assets(headers)

"""

def get_all_endpoint_assets(headers):

    """
    Sample function to get list of all
    endpoint assets in Runway
    """

    endpoint_assets_result = runway_obj.endpoint_asset.list(headers=headers)
    print(endpoint_assets_result)
