import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from time import sleep
import pandas as pd

# Initialize variables
website = 'https://twitter.com/login'
user_handle = "garyharris_wvua"  # Target user handle
all_tweets = set()  # Use a set to avoid duplicates

# Function to generate date ranges for each 3-month interval
def generate_date_ranges(start_date, end_date, interval_months=3):
    date_ranges = []
    while start_date < end_date:
        interval_end = start_date + timedelta(days=interval_months * 30)
        if interval_end > end_date:
            interval_end = end_date
        date_ranges.append((start_date, interval_end))
        start_date = interval_end + timedelta(days=1)
    return date_ranges

# Set up the date ranges
start_date = datetime(2019, 1, 11)
end_date = datetime(2024, 8, 8)
date_ranges = generate_date_ranges(start_date, end_date)

# Function to set up and log in to Twitter
def setup_and_login():
    driver = webdriver.Chrome()
    driver.get(website)

    # Login
    sleep(3)
    wait = WebDriverWait(driver, 20)
    username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
    username.send_keys('')  # Replace with your username
    next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
    next_button.click()

    sleep(3)
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys('')  # Replace with your password
    log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
    log_in.click()

    # Ensure login was successful
    sleep(5)
    print(driver.current_url)
    return driver

# Function to scrape tweets for a given date range
def scrape_tweets_for_date_range(driver, since_str, until_str):
    search_query = f"(from:{user_handle}) until:{until_str} since:{since_str}"
    driver.get(f"https://twitter.com/search?q={search_query}&f=live")
    sleep(5)

    # Check for "Retry" button at the start of search and restart if found
    try:
        retry_button = driver.find_element(By.XPATH, "//div[@role='button' and contains(text(),'Retry')]")
        if retry_button:
            print("Retry button found at the start of search. Restarting browser...")
            raise Exception("Retry at start")
    except selenium.common.exceptions.NoSuchElementException:
        pass

    scroll_attempts = 0
    max_scroll_attempts = 10  # Number of times to try scrolling to load more tweets
    tweets_collected = 0

    while scroll_attempts < max_scroll_attempts:
        tweet_elements = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
        new_tweets_collected = 0

        for tweet in tweet_elements:
            try:
                # Extract tweet text by concatenating all relevant spans and other elements
                tweet_text_elements = tweet.find_elements(By.XPATH, './/div[2]/div[2]//span')
                tweet_text = " ".join([element.text for element in tweet_text_elements]).strip()

                # Extract tweet date and URL
                tweet_date_elements = tweet.find_elements(By.XPATH, ".//time")
                tweet_date = tweet_date_elements[0].get_attribute("datetime") if tweet_date_elements else None
                tweet_url = tweet_date_elements[0].find_element(By.XPATH, "..").get_attribute('href') if tweet_date_elements else None

                # Only add tweet if it has text, URL, and date
                if tweet_text and tweet_url and tweet_date:
                    if (tweet_text, tweet_url, tweet_date) not in all_tweets:
                        all_tweets.add((tweet_text, tweet_url, tweet_date))  # Add to set to avoid duplicates
                        new_tweets_collected += 1

                        # Print tweet details
                        print("Tweet text:", tweet_text)
                        print("Tweet URL:", tweet_url)
                        print("Tweet Date:", tweet_date)
                        print("-------------------------")

            except selenium.common.exceptions.StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Skipping this tweet.")
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

        # Check for "Retry" button and click it if found
        try:
            retry_button = driver.find_element(By.XPATH, "//div[@role='button' and contains(text(),'Retry')]")
            if retry_button:
                retry_button.click()
                print("Retry button clicked, waiting for the page to reload...")
                sleep(10)  # Increase sleep to ensure the page reloads fully
        except selenium.common.exceptions.NoSuchElementException:
            pass

        # Scroll down slowly
        driver.execute_script('window.scrollBy(0, document.body.scrollHeight / 4);')
        sleep(17)  # Increase sleep time to slow down scrolling

        # If no new tweets were collected in this scroll, increment scroll_attempts
        if new_tweets_collected == 0:
            scroll_attempts += 1
        else:
            scroll_attempts = 0
            tweets_collected += new_tweets_collected

    return tweets_collected

# Main scraping loop
try:
    driver = setup_and_login()
    months_processed = 0

    for since_date, until_date in date_ranges:
        # Format the dates as strings
        since_str = since_date.strftime("%Y-%m-%d")
        until_str = until_date.strftime("%Y-%m-%d")

        # Scrape tweets for the current 3-month period
        while True:
            try:
                tweets_collected = scrape_tweets_for_date_range(driver, since_str, until_str)
            except Exception as e:
                print(f"Encountered an issue: {e}. Restarting browser...")
                driver.quit()
                sleep(300)  # Pause for 5 minutes before restarting the browser
                driver = setup_and_login()
                continue

            # If fewer than 30 tweets were collected, restart the browser and retry the same period
            if tweets_collected < 15:
                print(f"Collected only {tweets_collected} tweets for the period {since_str} to {until_str}. Restarting browser and retrying...")
                driver.quit()
                sleep(300)  # Pause for 5 minutes before restarting the browser
                driver = setup_and_login()
            else:
                print(f"Collected {tweets_collected} tweets for the period {since_str} to {until_str}.")
                break  # Move to the next period if enough tweets are collected

        # Increment the months processed counter
        months_processed += 3

        # After 6 months of data collection, close and reopen the browser
        if months_processed >= 6:
            print("Processed 6 months of data. Restarting browser...")
            driver.quit()
            sleep(300)  # Pause for 5 minutes before restarting the browser
            driver = setup_and_login()
            months_processed = 0

finally:
    # Save tweets to a CSV file
    all_tweets_list = list(all_tweets)
    if all_tweets_list:
        df_tweets = pd.DataFrame(all_tweets_list, columns=['Tweet', 'URL', 'Date'])
        csv_filename = r'D:\News Project\all the data sets\x data of wvua23\garyharris_wvua\selinium\harry_tweets_sel18.csv'
        df_tweets.to_csv(csv_filename, index=False)
        print(f"Saved {len(df_tweets)} tweets to {csv_filename}")
    else:
        print("No tweets were collected.")

    # Close the browser
    driver.quit()

