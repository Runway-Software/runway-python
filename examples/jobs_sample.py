import runway.sdk.models as models
from runway.sdk import PyRunway

# Basic setup to connect to Runway REST API
runway_obj = PyRunway()
login_request = models.LoginRequest(remember=True,email="<email address>",password="<password>")
authentication_result = runway_obj.authentication.login(request=login_request)
session_id = authentication_result.session
headers = {"Authorization" : "Session " + session_id}

"""
Example calls for these functions

get_all_jobs(headers)
create_job(headers,"Test Job 2",True,False,"Sample SDK Job Creation 2",[])
delete_job_by_id(headers,"6319a1d8-2469-4f5a-b586-c11cf7a97353")

"""

def get_all_jobs(headers):

    """
    Sample function to get a list of all existing
    jobs in Runway and print their attributes
    """

    job_list_result = runway_obj.job.list(headers=headers)
    for job in job_list_result.items:
        print()
        print("JOB: ")
        print(job)
        print("JOB SCHEDULE: ")
        print(job.schedule)
        print()


def create_job(headers,name,is_enabled,is_hidden,description,actions):

    """
    Sample function to create a job in
    Runway using the SDK
    """

    request = models.CreateJobRequest(is_enabled=is_enabled,name=name,is_hidden=is_hidden,description=description,actions=actions)
    job_create_result = runway_obj.job.create(request=request,headers=headers)

    print(job_create_result)


def delete_job_by_id(headers,id):

    """
    Sample function to delete a job in Runway
    using the SDK
    """

    job_delete_result = runway_obj.job.delete_by_id(job_id=id,headers=headers)
    print(job_delete_result)
