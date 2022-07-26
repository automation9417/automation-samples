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
