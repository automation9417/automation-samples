from clicknium import clicknium, locator
from clicknium.core.models.web.browsertab import BrowserTab
from get_channel_member_list import get_member_list
from get_channel_memeber_list_email import get_member_list_email
from sign_in_with_google import google_sign_in
from sign_in_with_slack_email import slack_email_sign_in
from clicknium.common.enums import *
#define sign method name
slack_email_sign_in_name="slack_email"
google_sign_name="google"

#Sign config
sign_method_name="" #google for Google account, slack_email for slack email.
sign_in_email_or_phone="" #google email or slack email
sign_in_password="" #account passwword

#slack config
slack_community_url="" #The URL of the slack community you want to send essage. e.g."https://example.slack.com"
slack_channel_name="" #The name of the channel you want to send message.

def open_slack_app_site()->BrowserTab:
    browser_tab=clicknium.chrome.open(slack_community_url)
    browser_tab.activate()
    return browser_tab

def close_open_desk():
    open_slack_cancel_btn= clicknium.wait_appear(locator.desktops.chrome.open_slack_win_cancel_btn,wait_timeout=10)  
    if open_slack_cancel_btn:
        print("Click cancel open slack desktop button.")
        open_slack_cancel_btn.click(by=MouseActionBy.MouseEmulation)   
    else:
        print("Cancle open slack desktop button not found, skip.")

def use_slack_in_browser():
    print("Click use slack in browser button.")
    use_slack_in_browser_button=clicknium.wait_appear(locator.websites.slack.use_slack_in_browser_button,wait_timeout=5)      
    if use_slack_in_browser_button:
        use_slack_in_browser_button.click()
    else:
        print("use slack in browser button not found.")

def sign_out():
    print("Start sign out.")
    user_avatar_btn=clicknium.wait_appear(locator.websites.app_slack.user_avatar_btn,wait_timeout=3)
    if user_avatar_btn:
        print("Click user avatar button.")
        user_avatar_btn.click()
        print("Click sign out button.")
        clicknium.find_element(locator.websites.app_slack.sign_out_btn).click()
    else:
        print("Not sign in.")

def sign_in_slack():
    print("sign in with "+sign_method_name)
    if sign_method_name == google_sign_name:
        google_sign_in(sign_in_email_or_phone,sign_in_password)
    elif sign_method_name == slack_email_sign_in_name:
        slack_email_sign_in(sign_in_email_or_phone,sign_in_password)
    else:
        raise("not supported sign in method:"+sign_method_name)

def sign_in()->BrowserTab:
    browser_tab=open_slack_app_site()
    print("Wait slack sign button.")
    slack_signin_btn=clicknium.wait_appear(locator.websites.slack.slack_signin_btn,wait_timeout=5) 
    if not slack_signin_btn:
        sign_out()
    sign_in_slack()
    close_open_desk()
    use_slack_in_browser()
    return browser_tab

def main():
    print("start main")
    browser_tab=sign_in()
    auth_error_notice=clicknium.wait_appear(locator.websites.oauth_slack.error_notice,wait_timeout=5)
    if auth_error_notice:
        print("auth error, try to sign again.")
        browser_tab.close()
        browser_tab=sign_in()
    else:
        print("auth success, start get channel member info.")

    member_list_csv_file_name=get_member_list(slack_channel_name)     
    members_email_csv_file=get_member_list_email(slack_channel_name,member_list_csv_file_name)
    print("Members email csv file:"+members_email_csv_file)
    print("Close browser.")
    browser_tab.close()

if __name__ == "__main__":
    main()