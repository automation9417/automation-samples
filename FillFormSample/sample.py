from clicknium import clicknium as cc, locator, ui

tab = cc.chrome.open("https://lincdoc.ou.edu/lincdoc/doc/run/ouathletics/OU_AdvisingForm2#ldTimeoutUri")
tab.find_element(locator.chrome.lincdoc.text_advising_unit).set_text("Athletics-OMS 256/(405) 325-8373")
tab.find_element(locator.chrome.lincdoc.text_advising_name).set_text("AJ Tierney__ajtierney@ou.edu")

tab.find_element(locator.chrome.lincdoc.text_student_id).set_text("student1")
tab.find_element(locator.chrome.lincdoc.text_first_name).set_text("tom")
tab.find_element(locator.chrome.lincdoc.text_last_name).set_text("jack")
tab.find_element(locator.chrome.lincdoc.text_phone_number).set_text("12345")
tab.find_element(locator.chrome.lincdoc.text_ou_email).set_text("test@lincdoc.ou.edu")
tab.find_element(locator.chrome.lincdoc.text_student_id).set_text("Junior")

tab.find_element(locator.chrome.lincdoc.checkbox_topic, {'topic':'Academic Contract'}).set_checkbox()

print('done')