from clicknium import clicknium as cc, ui, locator

if cc.chrome.extension.install_or_update():
    print("Please open chrome browser to enable Clicknium extension, then run sample again.")
else:
    tab = cc.chrome.open(url="https://www.linkedin.com/in/williamhgates/details/education/")
    
    for e in tab.find_elements(locator.chrome.linkedin.name):
        n = e.get_text().strip()    
        n = n[:int(len(n)/2)]
        print(n)
    for y in tab.find_elements(locator.chrome.linkedin.year):
        t = y.get_text().strip()
        t = t[:int(len(t)/2)]
        print(t)