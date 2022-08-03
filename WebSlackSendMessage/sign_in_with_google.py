from msilib.schema import Error
from clicknium import clicknium, locator

def google_sign_in(email,password):
    print("start sign in with google.")
    print("Click sign in with google.")
    clicknium.find_element(locator.websites.slack.google_sign_in_btn).click()
    print("Enter email or password.")
    choose_account_lebel=clicknium.wait_appear(locator.websites.google_account.choose_account_label,wait_timeout=5)
    if choose_account_lebel:
        print("Use another account to sign in.")
        print("Click use another account")
        clicknium.find_element(locator.websites.google_account.use_another_account_btn).click()
    else:
        print("sign in directly.")
    email_or_phone_input=clicknium.wait_appear(locator.websites.google_account.email_or_phone_input,wait_timeout=5)
    if email_or_phone_input:
        print("email_or_phone_input successfully found.")
        email_or_phone_input.set_text(email)
    else:
        error_msg="email_or_phone_input not found."
        print(error_msg)
        raise Error(error_msg)
    print("Click next.")
    clicknium.find_element(locator.websites.google_account.email_or_phone_next_btn).click()
    print("Enter password.")
    password_input=clicknium.wait_appear(locator.websites.google_account.password_input,wait_timeout=5)
    if password_input:
        print("password_input successfully found.")
        password_input.set_text(password)
    else:
        error_msg="password_input not found."
        print(error_msg)
        raise Error(error_msg)
    print("Click next to sign in.")
    clicknium.find_element(locator.websites.google_account.password_next_btn).click()
