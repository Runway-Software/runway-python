import runway.sdk.models as models
from runway.sdk import PyRunway

runway_obj = PyRunway(email="<email address>", password="<password>")

"""
Example calls for these functions

get_all_jobs(headers)
create_job(headers,"Test Job 2",True,False,"Sample SDK Job Creation 2",[])
delete_job_by_id(headers,"6319a1d8-2469-4f5a-b586-c11cf7a97353")

"""

def get_all_jobs():

    """
    Sample function to get a list of all existing
    jobs in Runway and print their attributes
    """

    job_list_result = runway_obj.job.list()
    for job in job_list_result.items:
        print()
        print("JOB: ")
        print(job)
        print("JOB SCHEDULE: ")
        print(job.schedule)
        print()


def create_job(name,is_enabled,is_hidden,description,actions):

    """
    Sample function to create a job in
    Runway using the SDK
    """

    request = models.createJobRequest(is_enabled=is_enabled,name=name,is_hidden=is_hidden,description=description,actions=actions)
    job_create_result = runway_obj.job.create(request=request)

    print(job_create_result)


def delete_job_by_id(id):

    """
    Sample function to delete a job in Runway
    using the SDK
    """

    job_delete_result = runway_obj.job.delete_by_id(jobid=id)
    print(job_delete_result)


get_all_jobs()
