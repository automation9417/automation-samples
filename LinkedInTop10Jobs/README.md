# Automatically Get Top 10 Jobs from LinkedIn Using Python Sample

## Setup

1. System requirements

- Windows 7 SP1 or above, windows 10 or 11 is recommended
- Python 3.7 or above.

2. Install the dependencies needed to run the sample

```
pip install -r requirements.txt
```

or 

```
pip install clicknium
pip install pywin32
```

3. Install Clicknium Chrome extension, about the installation refer to [Chrome Extension](https://www.clicknium.com/documents/tutorial/extensions/chromeextension)

```
from clicknium import clicknium as cc
cc.chrome.extension.install()
```

## How to run

1. Modify configuration file 'setting.json' to update the content with your information
```
{
    "linkedin_login_name": "your account username",
    "linkedin_login_password": "your account password",
    "linkedin_search_job_key": "your desired job title",
    "linkedin_search_job_location": "your desired job location",
    "result_csv_file": "C:\\test\\test.csv"
}
```
2. Run the sample
```
python sample.py
```
