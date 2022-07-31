import csv
from time import sleep
from clicknium import clicknium, locator,ui
from channel_operations import browse_channels, open_member_list_win, search_and_select_channel
def get_member_count()->int:
    print("Get member count.")
    sleep(2)
    member_count=clicknium.find_element(locator.websites.app_slack.channel_member_count_span).get_text()
    print("member count:"+member_count)
    member_count_int=0
    try:
        member_count_int=int(member_count.strip(' ').replace(',',''))
    except:
        print("Get member count again.")
        member_count=clicknium.find_element(locator.websites.app_slack.channel_member_count_span).get_text()
        print("member count:"+member_count)
        member_count_int=int(member_count.strip(' ').replace(',',''))
    return member_count_int

def get_member_list(channel_name) -> str:
    print("Get member list for "+channel_name)
    browse_channels()
    search_and_select_channel(channel_name)
    member_count=get_member_count()
    open_member_list_win()

    print("Focus channel member search box.")
    clicknium.find_element(locator.websites.app_slack.channel_member_search_box).set_focus()
    print("Wait add people appear.")
    add_peeple_btn=clicknium.wait_appear(locator.websites.app_slack.add_peeple_btn)
    if add_peeple_btn:
        print("Sent Down hot key.")
        clicknium.send_hotkey('{DOWN}')
        print("sleep 1 second.")
        sleep(1)
    else:
        msg="Add people button not found."
        print(msg)
        raise(msg)

    member_name_label_first=clicknium.wait_appear(locator.websites.app_slack.member_name_label_first)
    if not member_name_label_first:
        msg="Member name label first not found."
        print(msg)
        raise(msg)

    csv_file_name=channel_name+'_names.csv'    
    print("Save names to csv file:"+csv_file_name)
    with open(csv_file_name, 'w',encoding='utf-8', newline='') as csvfile:
        print("Set csv field names.")
        fieldnames = ['name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        print("Csv write header.")
        writer.writeheader()

        print("Start get channel names.")
        for num in range(1,member_count+1):
            print("Loop count:"+str(num))
            print("Sent Down hot key.")
            clicknium.send_hotkey('{DOWN}')
            sleep(1)
            print("Get current selected member's name.")
            name=clicknium.find_element(locator.websites.app_slack.member_name_label_focus).get_text()
            print("Write name " +name+" to csv.")
            writer.writerow({'name': name})         

    print("Click close member list window.")
    clicknium.find_element(locator.websites.app_slack.member_list_win_close_btn).click()
    print("Return filename.")
    return csv_file_name