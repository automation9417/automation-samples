from operator import contains
from time import sleep
from clicknium import clicknium as cc, locator, ui
from clicknium.common.enums import *
import json
import os
import scapingContactList

def scrape_contact_detail(group, channel):
    names = []
    if os.path.exists("data.json"):
        with open("data.json", 'r') as myfile:
            data=myfile.read()
            # parse file
            names = json.loads(data)

    params = {'group':group, 'channel':channel}
    ui(locator.slack.tabitem_group, {'group':group}).click()
    if not cc.is_existing(locator.slack.treeitem_channel, params):
        ui(locator.slack.treeitem_parent).click()
    ui(locator.slack.treeitem_channel, params).click()
    sleep(1)
    step = 0
    for item in names:
        if len(item['email']) == 0:
            ui(locator.slack.text_all, params).click()
            ui(locator.slack.edit_membername).set_text(item['name'], "set-text")
            member1 = cc.wait_appear(locator.slack.listitem_member1, {'name':item['name']})
            if member1 != None:
                member1.click()
            else:
                print("failed to search the member")
                item['email'] = "ignore"
                item['postfix'] = ""
                ui(locator.slack.image).click()
                continue

            try:
                email = ui(locator.slack.text_email).get_text(timeout=5)
                item['email'] = email
                item['postfix'] = email.split('@')[1]
            except:
                print("failed to find the email")
                item['email'] = "ignore"
                item['postfix'] = ""
                if cc.is_existing(locator.slack.image):
                    ui(locator.slack.image).click()
                    continue
            step += 1
            if step % 20 == 0:
                scapingContactList.SaveToFile(names)
            ui(locator.slack.close_image).click()
    scapingContactList.SaveToFile(names)

if __name__ == "__main__":
    group = "Python Developers"
    channel = "announcements"
    scrape_contact_detail(group, channel)