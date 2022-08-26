# spotify robot

I want to scrape a Spotify playlist from web page, at first I try to use selenium, but it is not obtaining the full list, as the song list  is dynamic loaded, I must scroll down to the bottom, then it can load all songs.

Finally I find one Visual Studio Code automation development tool, [clicknium](https://marketplace.visualstudio.com/items?itemName=ClickCorp.clicknium) (it should be new in 2022), it is really easy to use and one click to locate the ui element.
I just need record two locators and write several lines of python code, the job is accompolished.

As the list is dynamic loaded, I use iterate index to search each item, as [clicknium](https://www.clicknium.com) can automatically scroll the item into view, it will trigger to load new items, so I don't need take care about the dynamic loading.


I use parametric locator for title and author

![title](img/title.png)

![author](img/auther.png)

As one itme may has multiple authors, so I use the following code to get multiple author's name and link:
```python
    element = tab.find_element(locator.chrome.open.div_author, {'index':index})
    authers = element.children
    for item in element.children:
        artist.append(item.get_text())
        link.append(item.get_property('href'))
```

If you want to try clicknium, you can get started with the video on clicknium official site.