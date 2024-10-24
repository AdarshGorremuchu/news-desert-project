# Twitter Scraping Script with Selenium

## Overview
This Python script scrapes tweets from a specific Twitter user (@garyharris_wvua) over a specified date range using Selenium. The script logs into Twitter, searches for tweets within set 3-month intervals, and collects the tweet text, URL, and posting date. The collected data is stored in a CSV file.

The script is designed to avoid duplicates, handle intermittent errors, and restart the browser as needed to ensure robust scraping over long periods.

Download and install Chrome WebDriver from: ChromeDriver.
-----
Configure WebDriver:

Ensure the Chrome WebDriver is available in your PATH or provide the correct path in the code.

Login Credentials:
-----
Replace the 'username' and 'password' in the setup_and_login function with your Twitter login credentials. You can replace these placeholders with environment variables for added security.

How It Works
-----
Date Range Generation: The script generates 3-month intervals between January 11, 2019, and August 8, 2024. These intervals are used to query tweets within each specific range.

Logging In: The script uses Selenium to log into Twitter using the provided credentials.

Scraping Tweets:
----------

For each 3-month interval, the script searches for tweets using Twitter's advanced search feature.
It collects the tweet text, URL, and date for all tweets found in that period, while handling any "Retry" buttons and intermittent errors.
Error Handling:

If the script encounters issues (e.g., a "Retry" button or network issue), it restarts the browser and resumes from where it left off.
The script also closes and reopens the browser after scraping 6 months of data to avoid potential session timeouts.

Saving Data:
----------

All collected tweets are stored in a CSV file, ensuring no duplicates are saved.
Key Features
Login Automation: Uses Selenium to automate the login process on Twitter.
3-Month Interval Scraping: Scrapes tweets in 3-month periods for more granular control and rate-limiting.
Retry Handling: Automatically handles Twitter's "Retry" button if it appears during scrolling.
Browser Restarts: Restarts the browser periodically to maintain a fresh session, ensuring long-running scraping operations work smoothly.
Duplicate Prevention: Stores tweets in a set to avoid collecting duplicate entries.
CSV Output: Saves the collected tweet data into a CSV file for easy analysis.
Usage

Check Output:
----------

After completion, check the output CSV file for the collected tweets.

Notes
----------
This script is dependent on the stability of Twitter's layout. Changes to the Twitter interface may require adjustments to the XPaths used for locating elements.
Twitter may restrict access or rate-limit scraping activities, so you may need to adjust the script's intervals or use proxies if you encounter such issues.
Try to get only like 2,3 years data at atime and also create a new 'X' account don't use your personal account.
