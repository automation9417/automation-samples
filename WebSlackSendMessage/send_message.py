from msilib.schema import Error
from clicknium import clicknium, locator
import pyperclip

def browse_channels():
    print("Wait channels menu.")
    channels_menu_outter_div=clicknium.wait_appear(locator.websites.app_slack.channels_menu_outter_div,wait_timeout=5) 
    if channels_menu_outter_div:
        print("Get channels data-qa-channel-section-collapsed property.")
        menu_collapsed=channels_menu_outter_div.get_property("data-qa-channel-section-collapsed")
        print("menu_collapsed:"+menu_collapsed)
        if menu_collapsed=="true":
            print("Click channels menu inner span.")
            clicknium.find_element(locator.websites.app_slack.channels_menu_inner_span).click()
    else:
        msg="channels menu not found."
        print(msg)
        raise Error(msg)

    print("Click add channel button.")
    clicknium.find_element(locator.websites.app_slack.add_channel_btn).click() 
    print("Click browser channel button.")
    clicknium.find_element(locator.websites.app_slack.browser_channel_btn).click()

def search_and_select_channel(channel_name):
    print("Enter channel name for search.")
    clicknium.find_element(locator.websites.app_slack.search_channel_tbx).set_text(channel_name)
    print("Click search button.")
    clicknium.find_element(locator.websites.app_slack.search_channel_btn).click()
    print("Wait search result appear.")
    matched_result_span=clicknium.wait_appear(locator.websites.app_slack.matched_result_span,{"channel_name": channel_name})
    if matched_result_span:
        print("Click matched channel.")
        matched_result_span.click()
    else:
        msg="No matched channel for "+channel_name
        print(msg)
        raise Error(msg)

def send_message(channel_name, message):
    browse_channels()
    search_and_select_channel(channel_name)
    print("Meesage input set focus.")
    clicknium.find_element(locator.websites.app_slack.channel_message_input).set_focus()
    print("Send Ctrl + A")
    clicknium.send_hotkey('{CTRL}A')
    print("Send Ctrl + X")
    clicknium.send_hotkey('{CTRL}X')
    print("Set message to clipboard.")
    pyperclip.copy(message)
    print("Send Ctrl + V")
    clicknium.send_hotkey('{CTRL}V')
    print("Click Send message.")
    clicknium.find_element(locator.websites.app_slack.send_message_btn).click()
