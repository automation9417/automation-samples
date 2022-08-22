import os
from clicknium import clicknium as cc, locator,ui

def upload(caption, video_file):
    tab = cc.chrome.attach_by_title_url(url="https://www.tiktok.com*")
    tab.goto("https://www.tiktok.com/upload?lang=en")

    tab.find_element(locator.chrome.tiktok.div).set_focus()
    cc.send_text(caption)
    tab.find_element(locator.chrome.tiktok.button_selectfile).click()
    ui(locator.chrome.edit_file).set_text(video_file, by='set-text')
    ui(locator.chrome.button_open).click(by='control-invocation')
    tab.find_element(locator.chrome.tiktok.button_post).wait_property('disabled', 'false', wait_timeout=120)
    tab.find_element(locator.chrome.tiktok.button_post).click()


if __name__ == "__main__":
    video_file = os.path.join(os.getcwd(), "media", "clicknium_introduction.mp4")
    upload('Clicknium introduction', video_file)