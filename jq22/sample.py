from datetime import datetime
from clicknium import clicknium as cc, locator

tab = cc.chrome.open("https://www.jq22.com/yanshi404")

print(datetime.now())
tab.find_element(locator.chrome.jq22.span).click(by='mouse-emulation')
print(datetime.now())
tab.find_element(locator.chrome.jq22.span1).click(by='mouse-emulation')
elem = tab.find_element(locator.chrome.jq22.div)
elem.highlight()
elem2 = tab.find_element(locator.chrome.jq22.div1)
elem2.highlight()
pos1 = elem.get_position()
print(pos1)
pos2 = elem2.get_position()
print(pos2)
elem.drag_drop(pos2.Right-pos1.Right)