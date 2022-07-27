from clicknium import clicknium, locator

def slack_email_sign_in(email,password):
    print ("sign in with slack email")
    print("Enter email address.")
    clicknium.find_element(locator.websites.slack.slack_email_input).set_text(email)
    print("Enter password.")
    clicknium.find_element(locator.websites.slack.slack_password_input).set_text(password)
    print("Click sign in button.")
    clicknium.find_element(locator.websites.slack.slack_signin_btn).click()
