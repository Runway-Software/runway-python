import runway.sdk.models as models
from runway.sdk import PyRunway

# Basic setup to connect to Runway REST API
runway_obj = PyRunway(email="pjv4yj@virginia.edu", password="Kali@0921")

"""
Example calls for these endpoint functions
get_all_endpoint_assets(headers)

"""

def get_all_endpoint_assets():

    """
    Sample function to get list of all
    endpoint assets in Runway
    """

    endpoint_assets_result = runway_obj.endpoint_asset.list()
    print(endpoint_assets_result)

get_all_endpoint_assets()
