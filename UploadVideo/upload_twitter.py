import os
from time import sleep
from clicknium import clicknium as cc, locator,ui

def upload(tweet, video_file):
    tab = cc.chrome.attach_by_title_url(url="https://*twitter.com/*")
    tab.goto("https://twitter.com/compose/tweet")

    tab.find_element(locator.chrome.twitter.div).set_focus()
    cc.send_text(tweet)
    tab.find_element(locator.chrome.twitter.svg).click()
    ui(locator.chrome.edit_file).set_text(video_file, by='set-text')
    ui(locator.chrome.button_open).click(by='control-invocation')
    tab.wait_appear(locator.chrome.twitter.video)
    tab.find_element(locator.chrome.twitter.span_tweet).click()

if __name__ == "__main__":
    video_file = os.path.join(os.getcwd(), "media", "short_introduction.mp4")
    upload('Clicknium introduction', video_file)