from time import sleep
from clicknium import clicknium, locator
from clicknium.common.enums import *
def google_sign_in(email_or_phone,password):
    print("Sign in with google account:"+email_or_phone)
    print("Click Log in button.")
    clicknium.find_element(locator.websites.twitter.login_btn).click()
    sleep(2)
    clicknium.send_hotkey("{ESC}")
    print("Wait continue with google button.")
    continue_with_google_btn=clicknium.wait_appear(locator.websites.twitter.continue_with_google_btn,wait_timeout=5)
    if continue_with_google_btn:
        print("Click continue with google button.")
        continue_with_google_btn.click(by= MouseActionBy.MouseEmulation)
    else:
        print("Continue with google button not found.")  
        print("Click continue as xxx button.")
        clicknium.find_element(locator.websites.twitter.continue_as_x_btn).click(by= MouseActionBy.MouseEmulation)
        print("Click Use other account button.")
        clicknium.find_element(locator.websites.google_accounts.use_other_account_btn).click()
    print("Enter email or phone.")
    clicknium.find_element(locator.websites.google_accounts.email_or_phone_input).set_text(email_or_phone)
    print("Click next button.")
    clicknium.find_element(locator.websites.google_accounts.email_or_phone_next_btn).click()
    print("Enter password.")
    clicknium.find_element(locator.websites.google_accounts.password_input).set_text(password)
    print("Click next button.")
    clicknium.find_element(locator.websites.google_accounts.password_next_btn).click()