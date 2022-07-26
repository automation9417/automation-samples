from time import sleep
from clicknium import clicknium as cc, locator, ui
from clicknium.common.enums import *
import json
import os,re

def scrape_contact_list(group, channel):
    params = {'group':group, 'channel':channel}
    ui(locator.slack.tabitem_group, {'group':group}).click()
    if not cc.is_existing(locator.slack.treeitem_channel, params):
        ui(locator.slack.treeitem_parent).click()
    ui(locator.slack.treeitem_channel, params).click()
    sleep(1)
    text = ui(locator.slack.text_all, params).get_text()
    index = text.find("members")
    count = int("".join(re.findall("\d+",text[0:index])))
    ui(locator.slack.text_all, params).click()

    ui(locator.slack.edit_membername).click(by='mouse-emulation')
    cc.send_hotkey("{DOWN}")

    step = 0
    names = []
    if os.path.exists("data.json"):
        with open("data.json", 'r') as myfile:
            data=myfile.read()
            # parse file
            names = json.loads(data)
    step = len(names)
    if step > 0:
        for _ in range(step):
            cc.send_hotkey("{DOWN}")

    while step < count:
        for i in range(1,13):
            dict = {"index":i}
            if not cc.is_existing(locator.slack.listitem_member, dict):
                continue
            elem_member = ui(locator.slack.listitem_member, dict)
            name = elem_member.get_text()
            if NotContains(names, name):
                names.append({'name':name,'email':'', 'postfix':''})
                step += 1
                if step % 100 == 0:
                    SaveToFile(names)

        ## move mouse down to trigger new data loaded for member list
        ui(locator.slack.edit_membername).click(by='mouse-emulation')
        for i in range(10):
            cc.send_hotkey("{DOWN}")
        
    SaveToFile(names)

def NotContains(names, name):
    for item in names:
        if item['name'] == name:
            return False
    return True

def SaveToFile(names):
    jsonString = json.dumps(names)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

if __name__ == "__main__":
    group = "Python Developers"
    channel = "announcements"
    scrape_contact_list(group, channel)