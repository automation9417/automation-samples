# Requirement Statements
Enter one keyword in YouTube to get the top 10 searching results and write them into a CSV file.
We can start this simple beginner process quickly with [Clicknium](https://www.clicknium.com/).

# Environment Preparations
- Windows 10
- Visual Studio Code 1.69.2
- Clicknium 0.1.2
- Python 3.10.5
- Chrome 103.0.5060.134
# Run this sample
- follow [clicknium getting started](https://www.clicknium.com/documents/quickstart) to set up develop environment.
- clone [sample repo](https://github.com/automation9417/automation-samples.git).
```
git clone https://github.com/automation9417/automation-samples.git
```
- open the folder 'YoutubeSearch' in Visual Studio code
- open `sample.py` in visual studio code.
- press `F5` to debug the sample or press `CTRL+F5` to run sample.
# Steps

1. Assume that YouTube is open, so you only need to enter the keywords in the search box.  
   ![](/YoutubeSearch/.locator/chrome_img/e7173ae3-6711-41fe-9103-1f9140d1f8f7.jpg)
2. Click the button "search"  
   ![](/YoutubeSearch/.locator/chrome_img/51e97ce7-435d-4dc3-a995-0d9899fa67d4.jpg)
3. Get the top 10 searching results.
4. traversal results and insert the titles to the two-dimensional arrays
5. After the traversal, write two-dimensional arrays directly to CSV file.

# Concepts
[Clicknium](https://www.clicknium.com/) provides excellent ways of the recorder and the concept of the Locator, which helps you finish developing efficiently without lots of details. Hence it is worth getting to know the concepts below.
1. [Locator](https://www.clicknium.com/documents/concepts/locator)
2. [Recorder](https://www.clicknium.com/documents/tutorial/recorder/)  
**functions involved**
3. [click](https://www.clicknium.com/documents/references/python/uielement/click)
4. [set_text](https://www.clicknium.com/documents/references/python/uielement/set_text)
5. [attach_by_title_url](https://www.clicknium.com/documents/references/python/webdriver/attach_by_title_url)

# Get Started
1. Create a new folder. Open Visual Studio Code and press the keyboard shortcut `Ctrl+Shift+P` to select [Clicknium: Sample](https://www.clicknium.com/documents/tutorial/vscode/project_management) and select the newly created folder.
2. pip install clicknium
3. Open sample.py and follow the steps above
   Attaching the complete code as below.
   ```python
   from clicknium import clicknium as cc, locator, ui
   import time
   import csv
   import os
   def main():
       try:
           tab = cc.chrome.attach_by_title_url(
               "YouTube", "https://www.youtube.com/")
           tab.find_element(locator.chrome.search_input).set_text(
               "rpa", overwrite=True)
           tab.find_element(locator.chrome.search_button).highlight(duration=3)
           tab.find_element(locator.chrome.search_button).click()
           result = tab.find_elements(locator.chrome.youtube.search_result_list)
           rpaArray = []
           for item in result:
               rpaArray.append([item.get_text()])
           write_csv(rpaArray)
       except Exception as e:
           print(e)
       finally:
           print('done')
   
   def write_csv(rows):
       csvFile = "youtube_rpa.csv"
       if os.path.exists(csvFile):
           os.remove(csvFile)
       with open(csvFile, mode="w", encoding="utf-8-sig", newline="") as f:
           writer = csv.writer(f)
           writer.writerows(rows)
   
   if __name__ == "__main__":
       main()
   ```
