from time import sleep
from clicknium import clicknium as cc, locator

tab = cc.chrome.open("https://whalewisdom.com/filer/berkshire-hathaway-inc#tabholdings_tab_link")
tab.find_element(locator.chrome.whalewisdom.button_25).click()
tab.find_element(locator.chrome.whalewisdom.a_50).click()

sleep(3) #wait for table laoded

elems_sector = tab.find_elements(locator.chrome.whalewisdom.td_informationtechnology)
elemns_shares = tab.find_elements(locator.chrome.whalewisdom.td_890923410)

count = len(elems_sector)
for idx in range(count):
    sector = elems_sector[idx].get_text()
    shares = elemns_shares[idx].get_text()
    print({'sector': sector, 'shares': shares})