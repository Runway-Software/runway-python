import runway.sdk.models as models
from runway.sdk import PyRunway

# Basic setup to connect to Runway REST API
runway_obj = PyRunway()
login_request = models.LoginRequest(remember=True,email="<email address>",password="<password>")
authentication_result = runway_obj.authentication.login(request=login_request)
session_id = authentication_result.session
headers = {"Authorization" : "Session " + session_id}

"""
Example calls for these user functions

user_all(headers)
user_count(headers)

"""

def user_all(headers):

    """
    Sample function to get list of All
    users in Runway instancew
    """

    user_all_result = runway_obj.user.list(headers=headers)

    for user in user_all_result.items:
        print()
        print("User: " + user.name)
        print("id: " + user.id)
        print("Email Address: " + user.email_address)
        print("Company: " + user.company)
        print()



def user_count(headers):

    """
    Sample function to get current user
    count in Runway
    """

    user_count_result = runway_obj.user.count(headers=headers)

    print(user_count_result)
