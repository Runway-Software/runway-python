import runway.sdk.models as models
from runway.sdk import PyRunway

runway_obj = PyRunway(email="<email address>", password="<password>")

"""
Example calls for these user functions

user_all(headers)
user_count(headers)

"""

def user_all():

    """
    Sample function to get list of All
    users in Runway instancew
    """

    user_all_result = runway_obj.user.list()

    for user in user_all_result.items:
        print()
        print("User: " + user.name)
        print("id: " + user.id)
        print("Email Address: " + user.email_address)
        print("Company: " + user.company)
        print()



def user_count():

    """
    Sample function to get current user
    count in Runway
    """

    user_count_result = runway_obj.user.count()

    print(user_count_result)


user_all()
