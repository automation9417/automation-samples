from clicknium import clicknium as cc, locator

tab = cc.chrome.open("https://open.spotify.com/playlist/6iwz7yurUKaILuykiyeztu")
index = 2

titles = []
artists = []
links = []
while True:
    if not tab.is_existing(locator.chrome.open.div_title, {'index':index}):
        break
    title = tab.find_element(locator.chrome.open.div_title, {'index':index}).get_text()
    artist = []
    link = []
    element = tab.find_element(locator.chrome.open.div_auther, {'index':index})
    authers = element.children
    for item in element.children:
        artist.append(item.get_text())
        link.append(item.get_property('href'))

    titles.append(title)
    artists.append(artist)
    links.append(link)
    index += 1
tab.close()

print(titles)
print(artists)
print(links)

