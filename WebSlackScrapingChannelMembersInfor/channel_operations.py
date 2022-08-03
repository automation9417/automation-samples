from msilib.schema import Error
from time import sleep
from clicknium import clicknium, locator

def open_member_list_win():
    print("Click channel memeber count span.")
    clicknium.find_element(locator.websites.app_slack.channel_member_count_span).click()
    member_list_win_members_tab=clicknium.wait_appear(locator.websites.app_slack.member_list_win_members_tab)
    if member_list_win_members_tab:
        print("Click members tab in member list window.")
        member_list_win_members_tab.click()
    else:
        msg="members tab not found."
        print(msg)
        raise Error(msg)

def browse_channels():
    print("Wait channels menu.")
    channels_menu_inner_span=clicknium.wait_appear(locator.websites.app_slack.channels_menu_inner_span,wait_timeout=5) 
    if channels_menu_inner_span:
        print("Send hot key Ctrl+Shift+L to open browse channel page")
        clicknium.send_hotkey("{CTRL}{SHIFT}L")
        print("sleep 1 second")
        sleep(1)
    else:
        msg="channels menu not found."
        print(msg)
        raise Error(msg)

def search_and_select_channel(channel_name):
    print("Enter channel name for search.")
    clicknium.find_element(locator.websites.app_slack.search_channel_tbx).clear_text(by="set-text")
    clicknium.find_element(locator.websites.app_slack.search_channel_tbx).set_text(channel_name)
    print("Click search button.")
    clicknium.find_element(locator.websites.app_slack.search_channel_btn).click()
    clicknium.wait_appear(locator.websites.app_slack.matched_result_span,{"channel_name": channel_name})
    print("Click sort button.")
    clicknium.find_element(locator.websites.app_slack.channel_sort_btn).click()
    print("Click A to Z")
    clicknium.find_element(locator.websites.app_slack.sort_atoz_btn).click()
    print("Wait search result appear.")
    matched_result_span=clicknium.wait_appear(locator.websites.app_slack.matched_result_span,{"channel_name": channel_name})
    if matched_result_span:
        print("Click matched channel.")
        matched_result_span.click()
    else:
        msg="No matched channel for "+channel_name
        print(msg)
        raise Error(msg)