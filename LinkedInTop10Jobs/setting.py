import json

class Setting(object):
         
    with open("setting.json") as f:
        data = json.load(f)

    login_name = data['linkedin_login_name']

    login_password = data['linkedin_login_password']

    search_job_key = data['linkedin_search_job_key']

    search_job_location = data['linkedin_search_job_location']

    result_csv_file = data['result_csv_file']