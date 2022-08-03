from time import sleep
from clicknium import clicknium as cc, locator

def search_keyword(word):
    tab = cc.edge.open("www.stackoverflow.com")
    tab.find_element(locator.stackoverflow.text_q).set_text(word)
    tab.find_element(locator.stackoverflow.text_q).send_hotkey('{ENTER}')
    elem = tab.wait_appear(locator.stackoverflow.human_verification_div, wait_timeout=5)
    if elem != None:
        elem.click()

    tab.find_element(locator.stackoverflow.a_newest).click()
    
    catch_count = 0
    while catch_count < 30:
        sleep(1)
        elems_title = tab.find_elements(locator.stackoverflow.a_title)
        elems_vote = tab.find_elements(locator.stackoverflow.span_vote)
        elems_content = tab.find_elements(locator.stackoverflow.div_content)
        elems_time = tab.find_elements(locator.stackoverflow.span_time)
        for i in range(len(elems_title)):
            url = "https://www.stackoverflow.com" + elems_title[i].get_property('href')
            item = {
                'Keyword':word, 
                'Title': elems_title[i].get_text(), 
                'Content': elems_content[i].get_text(),
                'Time': elems_time[i].get_text(),
                'Vote': elems_vote[i].get_text(),
                'Url':url}
            print(item)
            catch_count += 1
        if tab.is_existing(locator.stackoverflow.a_next):
            tab.find_element(locator.stackoverflow.a_next).click()
        else:
            break
    tab.close()

search_keyword("selenium")