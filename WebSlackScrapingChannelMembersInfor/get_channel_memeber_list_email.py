import csv
from msilib.schema import Error
from threading import local
from clicknium import clicknium, locator 
from channel_operations import browse_channels, open_member_list_win, search_and_select_channel

def get_member_email(name) -> str:
    open_member_list_win()
    print("Set member in search text box.")
    clicknium.find_element(locator.websites.app_slack.channel_member_search_box).set_text(name)
    member_name_label=clicknium.wait_appear(locator.websites.app_slack.member_name_label_first,{"member_name":name},wait_timeout=5)
    email=None
    if member_name_label:
        print("Member name label normal successfully found.")
        print("Click member name label.")
        member_name_label.click()
        member_email_link=clicknium.wait_appear(locator.websites.app_slack.member_email_link,wait_timeout=5)
        if member_email_link:
            print("Member email link successfully found. Get email address.")
            email=member_email_link.get_text()
        else:
            print("Member email link not found.")
            email="email is not visible."
        print("Close user profile tab.")
        clicknium.find_element(locator.websites.app_slack.profile_close_btn).click()
    else:
        print("Member with name: "+name+" not found.")
        print("Click member list window close button.")
        email="user not found."
        clicknium.find_element(locator.websites.app_slack.member_list_win_close_btn).click()
      
    return email

def get_member_list_email(channel_name,name_list_csv_file) -> str:
    print("Get member list for "+channel_name)
    browse_channels()
    search_and_select_channel(channel_name)
    
    ret_csv_file_name=channel_name+'_member_emails.csv'
    print("Save member emails to csv file:"+ret_csv_file_name)
    with open(ret_csv_file_name, 'w',encoding='utf-8', newline='') as csvfile:
        print("Set csv field names.")
        fieldnames = ['name',"email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        print("Csv write header.")
        writer.writeheader()

        print("Read name list csv file:"+name_list_csv_file)
        with open(name_list_csv_file,encoding='utf-8', mode ='r')as file:
            print("Reading the CSV file.")
            csvFile = csv.reader(file)
            print("Start get email one by one.")
            index=-1
            for line in csvFile:
                index=index+1
                if index==0:
                    continue
                name=line[0]
                print("Start get the email of "+name)
                email=get_member_email(name)
                if email:
                    print("Write name:" +name+",email:"+email+" to csv.")
                    writer.writerow({'name': name,"email":email}) 
                else:
                    print("Email of "+name+" not found.")        

    print("Return filename:"+ret_csv_file_name)
    return ret_csv_file_name