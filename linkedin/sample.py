from clicknium import clicknium as cc, locator
from time import sleep
from clipboard import get_clipboard_data, clear_clipboard_data
from csvutils import list_dict_to_csv
from setting import Setting


def login():
    _tab.find_element(locator.chrome.linkedin.login.login_email).set_text(Setting.login_name)
    _tab.find_element(locator.chrome.linkedin.login.login_password).set_text(Setting.login_password)
    _tab.find_element(locator.chrome.linkedin.login.signin).click()
    _tab.wait_appear(locator.chrome.linkedin.login.skip_add_phone, wait_timeout = 5).click()

def search_jobs():
    _tab.wait_appear(locator.chrome.linkedin.job.jobs_channel, wait_timeout = 5).click()
    _tab.wait_appear(locator.chrome.linkedin.job.job_search_key, wait_timeout = 10).set_text(Setting.search_job_key)
    _tab.find_element(locator.chrome.linkedin.job.job_search_location).set_text(Setting.search_job_location)
    _tab.find_element(locator.chrome.linkedin.job.job_search).click()

def get_job_top10_list():
    job_list = []
    clear_clipboard_data()
    for i in range(1,11):
        ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_listitem, {"index": i}, wait_timeout = 5)
        if ele:
            details = {}
            # click job item
            ele.click()

            # get job's detail info: title, company name, company size, post date, job style, job link
            job_title_ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_title, wait_timeout = 5)
            if job_title_ele:
                details["Job Title"] = job_title_ele.get_text().strip()

            job_company_ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_company, wait_timeout = 2)
            if job_company_ele:
                details["Company Name"] = job_company_ele.get_text().strip()

            company_size_ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.company_size, wait_timeout = 2)
            if company_size_ele:
                scale = company_size_ele.get_text().strip() if "employees" in company_size_ele.get_text() else ""
                details["Company Size"] = scale

            job_post_date_ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_post_date, wait_timeout = 2)
            if job_post_date_ele:
                post_date = job_post_date_ele.get_text().strip() if "ago" in job_post_date_ele.get_text() else ""
                details["Post Date"] = post_date
            
            job_type_ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_type, wait_timeout = 2)
            if job_type_ele:
                details["Job Type"] = job_type_ele.get_text().strip()

            job_share_btn_ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.share_button, wait_timeout = 2)
            if job_share_btn_ele:
                job_share_btn_ele.click()
                copy_link = _tab.wait_appear(locator.chrome.linkedin.jobitem.copy_link, wait_timeout = 2)
                if copy_link:
                    copy_link.click()
                    sleep(0.2)
                    details["Job Link"] = get_clipboard_data()
            print(details)
            job_list.append(details)

    if job_list:
        list_dict_to_csv(job_list, Setting.result_csv_file)
                                        

if __name__ == "__main__":
    _tab = cc.chrome.open("https://www.linkedin.com/", is_wait_complete = True)
    if _tab.is_existing(locator.chrome.linkedin.login.login_email):
        login()    
    search_jobs()    
    get_job_top10_list()

