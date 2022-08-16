from datetime import datetime
from clicknium import clicknium as cc, locator

tab = cc.chrome.open("https://www.jq22.com/yanshi404")

print(datetime.now())
tab.find_element(locator.chrome.jq22.span).click(by='mouse-emulation')
print(datetime.now())
tab.find_element(locator.chrome.jq22.span1).click(by='mouse-emulation')
elem = tab.find_element(locator.chrome.jq22.div)
elem2 = tab.find_element(locator.chrome.jq22.div1)
pos1 = elem.get_position()
pos2 = elem2.get_position()
elem2.drag_drop(pos2.Right-pos1.Right)