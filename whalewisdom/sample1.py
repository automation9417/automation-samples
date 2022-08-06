from time import sleep
from clicknium import clicknium as cc, locator

tab = cc.chrome.open("https://whalewisdom.com/filer/berkshire-hathaway-inc#tabholdings_tab_link")

i = 0

while True:
    elems_sector = tab.find_elements(locator.chrome.whalewisdom.td_informationtechnology)
    elemns_shares = tab.find_elements(locator.chrome.whalewisdom.td_890923410)

    count = len(elems_sector)
    for idx in range(count):
        sector = elems_sector[idx].get_text()
        shares = elemns_shares[idx].get_text()
        print({'sector': sector, 'shares': shares})
    i += 1
    if i>1:
        break
    tab.find_element(locator.chrome.whalewisdom.a).click()
    sleep(2) #wait for table loaded
    