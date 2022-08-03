from distutils.fancy_getopt import FancyGetopt
from time import sleep
from msilib.schema import Error
from clicknium import clicknium, locator,ui
from clicknium.common.enums import *
import csv

def search_and_select_user(username):
    print("Click Explore menu.")
    clicknium.find_element(locator.websites.twitter.explore_menu).click()
    print("Click search text box.")
    clicknium.find_element(locator.websites.twitter.search_text_box_input).click(by= MouseActionBy.MouseEmulation)
    print("Enter username for search.")
    clicknium.find_element(locator.websites.twitter.search_text_box_input).set_text(username)
    print("Sleep 1 second.")
    sleep(1)
    print("Send hot key Enter")
    clicknium.send_hotkey('{ENTER}')
    
    print("Wait search people tab.")
    search_people_tab=clicknium.wait_appear(locator.websites.twitter.search_people_tab,wait_timeout=10)
    if search_people_tab:
        print("Click search people tab.")
        search_people_tab.click()
    else:
        msg="Search people tab not found."
        print(msg)
        raise Error(msg)
    
    print("Wait target search people.")
    target_search_people=clicknium.wait_appear(locator.websites.twitter.target_search_people,{"user_name":username}, wait_timeout=10)
    if target_search_people:
        print("Click target search people.")
        target_search_people.click()
    else:
        msg="People:"+username+" not found."
        print(msg)
        raise Error(msg)

def get_user_recent_tweets(username)->str:
    print("Start get tweets for:"+username)
    search_and_select_user(username)

    print("Click tweets tab.")
    clicknium.find_element(locator.websites.twitter.user_tweets_tab).click()
    print("Wait tweet appear.")
    tweet_article=clicknium.wait_appear(locator.websites.twitter.tweet_article, wait_timeout=10)
    if tweet_article:
        print("Tweet successfully found.")
    else:
        msg="Tweet not found."
        print(msg)
        raise Error(msg) 
       
    ret_csv_file_name=username+'_recent_tweets.csv'
    print("Save member emails to csv file:"+ret_csv_file_name)
    with open(ret_csv_file_name, 'w', newline='',encoding='utf-8') as csvfile:
        print("Set csv field names.")
        fieldnames = ['publish_date',"content","link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        print("Csv write header.")
        writer.writeheader()

        print("Get user tweets.")
        tweet_articles=clicknium.find_elements(locator.websites.twitter.tweet_article)
        total=0
        #Start for loop
        for index in range(1,tweet_articles.__len__()+1):
            print("Get tweet detail, index:"+str(index))
            selected_tweet_article=clicknium.wait_appear(locator.websites.twitter.selected_tweet_article,{"index":index},wait_timeout=5) 
            if not selected_tweet_article:      
                print("article not found. Index:"+str(index))
                continue
            print("Wait tweet text appear.")
            tweet_text=clicknium.wait_appear(locator.websites.twitter.tweet_text,{"index":index},wait_timeout=2) 
            content=""
            if tweet_text:
                print("Get tweet text content.")
                content=tweet_text.get_text()
                print("content: "+content)

            print("Wait tweet card appear.")
            tweet_card=clicknium.wait_appear(locator.websites.twitter.tweet_card,{"index":index},wait_timeout=2) 
            link=""
            if tweet_card:
                print("Get tweet card link.")
                link=tweet_card.get_property("href")
                print("link: "+link)
            
            print("Wait tweet publish date appear.")
            tweet_publish_date=clicknium.wait_appear(locator.websites.twitter.tweet_publish_date,{"index":index},wait_timeout=2) 
            publish_time=""
            if tweet_publish_date:
                print("Get tweet publish time.")
                publish_time=tweet_publish_date.get_property("datetime")
                print("publish_time: "+publish_time)
            
            print("Add to csv file")
            writer.writerow({'publish_date':publish_time,"content":content,"link":link}) 
            #End for loop

        total=total+index
        print("Get user recent tweets done. Total:"+str(total))
