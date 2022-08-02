from get_user_recent_tweets import get_user_recent_tweets
from sign_in_with_google import google_sign_in
from sign_in_with_twitter_account import sign_in_with_twitter_account
from clicknium.core.models.web.browsertab import BrowserTab
from clicknium import clicknium, locator,ui


twitter_explore_url="https://twitter.com/explore"

#define sign method name
twitter_account_sign_in_name="twiiter_account"
google_sign_in_name="google"

#Sign in config
sign_in_method_name="google" #google for Google account, twiiter_account for tweet account.
account="sharmajaafar1st@gmail.com" #google email/phone, twitter username/email/phone
verify_account=""#Sign in with tweet account, may need secondary verification. e.g. sign in with twitter email use username/phone to verify.
password="Xu@13524667596" # password
#Scraping user name
scrape_user_name="" # The Twitter name you want to scrape Tweets from, must start with @ e.g. @exemple

def open_twitter_explore()->BrowserTab:
    print("Open chrome Browser with:"+twitter_explore_url)
    browser_tab=clicknium.chrome.open(twitter_explore_url)
    print("Activate new opened browser tab.")
    browser_tab.activate()
    return browser_tab
def sign_out()->str:
    print("Wait twitter account options button.")
    account_options_btn=clicknium.wait_appear(locator.websites.twitter.account_options_btn,wait_timeout=5)
    if account_options_btn:
        print("Click twitter account options button.")
        account_options_btn.click()
        print("Click log out button.")
        clicknium.find_element(locator.websites.twitter.logout_btn).click()
        print("Click log out confirm button.")
        clicknium.find_element(locator.websites.twitter.logout_confirm_btn).click()
        logout_again_btn=clicknium.wait_appear(locator.websites.twitter.logout_again_btn,wait_timeout=5)
        if logout_again_btn:
            print("Click log out again button.")
            logout_again_btn.click()
        else:
            print("No need to click log out again.")
        return "Log out successfully."
    else:
        print("Twitter not sign in.")
        return None
def sign_in_twitter():
    print("sign in with "+sign_in_method_name)
    if sign_in_method_name == google_sign_in_name:
        google_sign_in(account,password)
    elif sign_in_method_name == twitter_account_sign_in_name:
        sign_in_with_twitter_account(account,verify_account,password)
    else:
        raise("not supported sign in method:"+sign_in_method_name)

def main():
    print("start main")
    tab=open_twitter_explore()
    sign_out_ret=sign_out()
    if sign_out_ret:
        print("Gogo the twitter explore after sign out")
        tab.goto(twitter_explore_url)
    sign_in_twitter()
    get_user_recent_tweets(scrape_user_name)
    sign_out()
    tab.close()

if __name__ == "__main__":
    main()