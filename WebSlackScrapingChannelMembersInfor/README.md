# Requirement Statements
Get member list of a slack community's channel and save to a CSV file.
We can start this simple beginner process quickly with [Clicknium](https://www.clicknium.com/).

# Environment Preparations
- Windows 10
- Visual Studio Code 1.69.2
- Clicknium 0.1.2
- Python 3.10.5
- Chrome 103.0.5060.134
> **Remarks:**  
>- Need run this sample in English region. 

# Run this sample
- Follow [clicknium getting started](https://www.clicknium.com/documents) to set up develop environment.
- Clone [sample repo](https://github.com/automation9417/automation-samples.git).
  ```
  git clone https://github.com/automation9417/automation-samples.git
  ```
- Open the folder 'WebSlackScrapingChannelMembersInfor' in Visual Studio code
- Open `sample.py` in visual studio code.
- Fill the sign config in  `sample.py`
  ```python
  sign_method_name="" #google for Google account, slack_email for slack email.
  sign_in_email_or_phone="" #google email or slack email
  sign_in_password="" #account passwword
  ```
- Fill the slack config in `sample.py`
  ```python
  slack_community_url="" #The URL of the slack community you want to send essage. e.g."https://example.slack.com"
  slack_channel_name="" #The name of the channel you want to send message.
  slack_message="" #The message content
  ```
- Press `F5` to debug the sample or press `CTRL+F5` to run sample.

# Steps

1. Assume Slack is not open in chrome, so we need open chrome with the community address firstly.  
   ```python
   #Use following code to open chrome with target url
   browser_tab=clicknium.chrome.open("https://example.slack.com") # update the address to your slack community.
   ```
2. Assume Slack is not signed in, so we need to sign in slack with Google account or Slack account.  
![](imgs/sign_in_slack.png)
  - Google account sign in
    ```python
    from msilib.schema import Error
    from clicknium import clicknium, locator
    def google_sign_in(email,password):
        clicknium.find_element(locator.websites.slack.google_sign_in_btn).click()
        choose_account_lebel=clicknium.wait_appear(locator.websites.google_account.choose_account_label,wait_timeout=5)
        if choose_account_lebel:
            clicknium.find_element(locator.websites.google_account.use_another_account_btn).click()
        email_or_phone_input=clicknium.wait_appear(locator.websites.google_account.email_or_phone_input,wait_timeout=5)
        if email_or_phone_input:
            email_or_phone_input.set_text(email)
        else:
            error_msg="email_or_phone_input not found."
            raise Error(error_msg)
        clicknium.find_element(locator.websites.google_account.email_or_phone_next_btn).click()
        password_input=clicknium.wait_appear(locator.websites.google_account.password_input,wait_timeout=5)
        if password_input:
            password_input.set_text(password)
        else:
            error_msg="password_input not found."
            raise Error(error_msg)
        clicknium.find_element(locator.websites.google_account.password_next_btn).click()
    ```
  - Slack account sign in
    ```python
    from clicknium import clicknium, locator

    def slack_email_sign_in(email,password):
        clicknium.find_element(locator.websites.slack.slack_email_input).set_text(email)
        clicknium.find_element(locator.websites.slack.slack_password_input).set_text(password)
        clicknium.find_element(locator.websites.slack.slack_signin_btn).click()
    ```
3. Cancel open slack desktop app  
![](imgs/cancle_open_slack_desktop.png)
  - Click `Cancel` button
      ```python
      from clicknium import clicknium, locator
      from clicknium.common.enums import *
      def close_open_desk():
          open_slack_cancel_btn= clicknium.wait_appear(locator.desktops.chrome.open_slack_win_cancel_btn,wait_timeout=10)  
          if open_slack_cancel_btn:
              open_slack_cancel_btn.click(by=MouseActionBy.MouseEmulation) 
      ```
4. Choose use slack in browser  
![](imgs/choose_use_slack_in_browser.png)  
  - Click `use Slack in your browser`
      ```python
      from clicknium import clicknium, locator
      def use_slack_in_browser():
          use_slack_in_browser_button=clicknium.wait_appear(locator.websites.slack.use_slack_in_browser_button,wait_timeout=5)      
          if use_slack_in_browser_button:
              use_slack_in_browser_button.click()
      ```    
5. Open search channel page.  
![](imgs/all_channels.png)  
  - Send hot key `Ctrl+Shift+L` to open search change page
    ```python
    def browse_channels():
        channels_menu_inner_span=clicknium.wait_appear(locator.websites.app_slack.channels_menu_inner_span,wait_timeout=5) 
        if channels_menu_inner_span:
            clicknium.send_hotkey("{CTRL}{SHIFT}L")
            sleep(1)
        else:
            msg="channels menu not found."
            raise Error(msg)
    ``` 
6. Search and select the target channel.  
![](imgs/slack_search_select_channel.png)  
  - Enter the target channel name  
  - Click the `Search` icon  
  - Choose sort `A to Z`  
  ![](imgs/choose_sort_way.png)  

  - Select the target channel  
    ```python
    from msilib.schema import Error
    from clicknium import clicknium, locator
    def search_and_select_channel(channel_name):
        clicknium.find_element(locator.websites.app_slack.search_channel_tbx).clear_text()
        clicknium.find_element(locator.websites.app_slack.search_channel_tbx).set_text(channel_name)
        clicknium.find_element(locator.websites.app_slack.search_channel_btn).click()
        clicknium.find_element(locator.websites.app_slack.channel_sort_btn).click()
        clicknium.find_element(locator.websites.app_slack.sort_atoz_btn).click()
        matched_result_span=clicknium.wait_appear(locator.websites.app_slack.matched_result_span,{"channel_name": channel_name})
        if matched_result_span:
            matched_result_span.click()
        else:
            msg="No matched channel for "+channel_name
            raise Error(msg)
    ```
7. Get channel member count.  
![](imgs/channel_member_count.png)  
  - Use [get_text](https://www.clicknium.com/documents/references/python/uielement/get_text) to get the member count  
    ```python
    from clicknium import clicknium, locator
    def get_member_count()->int:
        member_count=clicknium.find_element(locator.websites.app_slack.channel_member_count_span).get_text()
        member_count_int=0
        try:
            member_count_int=int(member_count.strip(' ').replace(',',''))
        except:
            member_count=clicknium.find_element(locator.websites.app_slack.channel_member_count_span).get_text()
            member_count_int=int(member_count.strip(' ').replace(',',''))
        return member_count_int
    ```
8. Open members list window
![](imgs/open_member_list_win.png)  
- Click `View members` to open the window
- Select the `Members` tab
  ```python
  from msilib.schema import Error
  from clicknium import clicknium, locator

  def open_member_list_win():
      clicknium.find_element(locator.websites.app_slack.channel_member_count_span).click()
      member_list_win_members_tab=clicknium.wait_appear(locator.websites.app_slack.member_list_win_members_tab)
      if member_list_win_members_tab:
          member_list_win_members_tab.click()
      else:
          msg="members tab not found."
          raise Error(msg)
  ```
9. Get members name one by one
![](imgs/get_member_name_one_by_one.png)  
- Focus the search text box
- Send `Down` hot key to select `Add People`
- Loop to get member name
  - Send `Down` hot key to select member
  - Use [get_text](https://www.clicknium.com/documents/references/python/uielement/get_text) to get the member name
  - Save name to CSV file  
- Close member list window
  ```python
  import csv
  from time import sleep
  from clicknium import clicknium, locator

  def get_member_list(channel_name) -> str:
      browse_channels()
      search_and_select_channel(channel_name)
      member_count=get_member_count()
      open_member_list_win()

      clicknium.find_element(locator.websites.app_slack.channel_member_search_box).set_focus()
      add_peeple_btn=clicknium.wait_appear(locator.websites.app_slack.add_peeple_btn)
      if add_peeple_btn:
          clicknium.send_hotkey('{DOWN}')
          sleep(1)
      else:
          msg="Add people button not found."
          raise(msg)

      member_name_label_first=clicknium.wait_appear(locator.websites.app_slack.member_name_label_first)
      if not member_name_label_first:
          msg="Member name label first not found."
          raise(msg)

      csv_file_name=channel_name+'_names.csv'    
      with open(csv_file_name, 'w',encoding='utf-8', newline='') as csvfile:
          fieldnames = ['name']
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
          writer.writeheader()

          for num in range(1,member_count+1):
              clicknium.send_hotkey('{DOWN}')
              sleep(1)
              name=clicknium.find_element(locator.websites.app_slack.member_name_label_focus).get_text()
              writer.writerow({'name': name})         

      clicknium.find_element(locator.websites.app_slack.member_list_win_close_btn).click()
      return csv_file_name
  ```
10. Get member email one by one
  - Loop  
    - Open members list window 
    ![](imgs/get_member_name_one_by_one.png)   
      ```python  
      open_member_list_win()
      ```  
    - Enter the member name to find member   
    - Click the target member to open the member profile  
    ![](imgs/open_member_profile.png)     
    - Use [get_text](https://www.clicknium.com/documents/references/python/uielement/get_text) to get the member email in profile section  
    - Close the member profile section  
    ![](imgs/get_email_from_profile.png)  
      ```python
      import csv
      from msilib.schema import Error
      from threading import local
      from clicknium import clicknium, locator 
      from channel_operations import browse_channels, open_member_list_win, search_and_select_channel

      def get_member_email(name) -> str:
          open_member_list_win()
          clicknium.find_element(locator.websites.app_slack.channel_member_search_box).set_text(name)
          member_name_label=clicknium.wait_appear(locator.websites.app_slack.member_name_label_first,{"member_name":name},wait_timeout=5)
          email=None
          if member_name_label:
              member_name_label.click()
              member_email_link=clicknium.wait_appear(locator.websites.app_slack.member_email_link,wait_timeout=5)
              if member_email_link:
                  email=member_email_link.get_text()
              else:
                  email="email is not visible."
              clicknium.find_element(locator.websites.app_slack.profile_close_btn).click()
          else:
              email="user not found."
              clicknium.find_element(locator.websites.app_slack.member_list_win_close_btn).click()
          return email

      def get_member_list_email(channel_name,name_list_csv_file) -> str:
          browse_channels()
          search_and_select_channel(channel_name)
          
          ret_csv_file_name=channel_name+'_member_emails.csv'
          with open(ret_csv_file_name, 'w',encoding='utf-8', newline='') as csvfile:
              fieldnames = ['name',"email"]
              writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
              writer.writeheader()

              with open(name_list_csv_file,encoding='utf-8', mode ='r')as file:
                  csvFile = csv.reader(file)
                  index=-1
                  for line in csvFile:
                      index=index+1
                      if index==0:
                          continue
                      name=line[0]
                      email=get_member_email(name)
                      if email:
                          writer.writerow({'name': name,"email":email}) 
          return ret_csv_file_name
      ```
8. Sign out.  
![](imgs/slack_sign_out.png)  
  - Click user avatar
  - Click `Sign out` 
    ```python
    from clicknium import clicknium, locator

    def sign_out():
        user_avatar_btn=clicknium.wait_appear(locator.websites.app_slack.user_avatar_btn,wait_timeout=5)
        if user_avatar_btn:
            user_avatar_btn.click()
            clicknium.find_element(locator.websites.app_slack.sign_out_btn).click()
    ```
11. Close opened browser tab.  
   ```python  
   browser_tab.close()# close the opened browser tab.
   ``` 
# Tips 
- Pass variable to the locator  
In this sample channel name is passed to the `matched_result_span` locator as following
  - Define variable in locator  
   ![](imgs/pass_variable.png)  
  -  Pass variable in code
      ```python
      matched_result_span=clicknium.wait_appear(locator.websites.app_slack.matched_result_span,{"channel_name": channel_name})
      ```
- Use wildcard in locator  
In this sample `channel_sort_btn` locator's sInfo is updated end with * as following
![](imgs/sort_btn_wildcard.png)  
# Concepts  
[Clicknium](https://www.clicknium.com/) provides excellent ways of the recorder and the concept of the Locator, which helps you finish developing efficiently without lots of details. Hence it is worth getting to know the concepts below.
1. [Locator](https://www.clicknium.com/documents/concepts/locator)
2. [Recorder](https://www.clicknium.com/documents/tutorial/recorder/)  
> **Functions involved**
>- [click](https://www.clicknium.com/documents/references/python/uielement/click)
>- [set_text](https://www.clicknium.com/documents/references/python/uielement/set_text)
>- [get_text](https://www.clicknium.com/documents/references/python/uielement/get_text)
>- [open browser](https://www.clicknium.com/documents/references/python/webdriver/open)
>- [wait_appear](https://www.clicknium.com/documents/references/python/globalfunctions/wait_appear)
>- [activate browser tab](https://www.clicknium.com/documents/references/python/webdriver/browser/browsertab/activate)
>- [close browser tab](https://www.clicknium.com/documents/references/python/webdriver/browser/browsertab/close)
>- [find_element](https://www.clicknium.com/documents/references/python/webdriver/browser/browsertab/find_element)
>- [set_focus](https://www.clicknium.com/documents/references/python/uielement/set_focus)
>- [get_property](https://www.clicknium.com/documents/references/python/uielement/get_property)
>- [send_hotkey](https://www.clicknium.com/documents/references/python/uielement/send_hotkey)   
# Get Started
1. Create a new folder. Open Visual Studio Code and press the keyboard shortcut `Ctrl+Shift+P` to select [Clicknium: Sample](https://www.clicknium.com/documents/tutorial/vscode/project_management) and select the newly created folder.
2. pip install clicknium
3. pip install pyperclip
4. Copy the '.locator' folder under 'WebSlackSendMessage' to your new created folder
5. Open `sample.py` and follow the steps above