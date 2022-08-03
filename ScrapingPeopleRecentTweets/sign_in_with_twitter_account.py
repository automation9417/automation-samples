from time import sleep
from clicknium import clicknium, locator
from clicknium.common.enums import *

def sign_in_with_twitter_account(email_or_phone_or_username,verify_account,password):
    print("Sign in with twitter account:"+email_or_phone_or_username)
    print("Click Log in button.")
    clicknium.find_element(locator.websites.twitter.login_btn).click()
    print("Wait Sign as window cancel button.")
    sleep(2)
    clicknium.send_hotkey("{ESC}")
    print("Enter Phone, email, or username.")
    clicknium.find_element(locator.websites.twitter.twitter_account_input).set_text(email_or_phone_or_username)
    print("Click Next button.")
    clicknium.find_element(locator.websites.twitter.login_next_btn).click()
    print("Wait twitter verify input.")
    twitter_verify_input=clicknium.wait_appear(locator.websites.twitter.twitter_verify_input,wait_timeout=5)
    if twitter_verify_input:
        print("Enter verify account:"+verify_account)
        twitter_verify_input.set_text(verify_account)
        print("Click Next button.")
        clicknium.find_element(locator.websites.twitter.login_next_btn).click()
    else:
        print("Twitter verify account input not found.")
    print("Enter password.")
    clicknium.find_element(locator.websites.twitter.twitter_password_input).set_text(password)
    print("Click Login button in Login Form.")
    clicknium.find_element(locator.websites.twitter.login_form_login_btn).click()