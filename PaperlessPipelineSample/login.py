from clicknium import clicknium as cc, locator, ui

# Open a browser
tab = cc.edge.open("https://app.paperlesspipeline.com/")

# Fill in the email and password
tab.find_element(locator.plp.login.email).set_text("user@contoso.com")
tab.find_element(locator.plp.login.password).set_text("password")

# Click "Login" button
tab.find_element(locator.plp.login.login).click()