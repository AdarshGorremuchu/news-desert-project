Project Overview
This Python script is designed to scrape articles from all sections of the WVUA23 website. The script extracts information such as the article title, description, publication date, author, tags, and categories from multiple pages and saves the data in a CSV file.
------------
Features
Scrapes multiple pages of articles automatically.
Extracts title, description, publication date, author, tags, and categories for each article.
Combines content from paragraphs and list items into a single description.
Saves the collected data into a CSV file for further analysis.
Requirements
To run this script, you will need the following Python libraries installed:
requests: To make HTTP requests to the website.
beautifulsoup4: For parsing the HTML content.
pandas: To store and manipulate the scraped data in a CSV file.
-------------
How It Works
Scrape Pagination: The script first determines the total number of pages by analyzing the pagination element on the website.
Extract Article URLs: For each page, the script retrieves all article URLs by locating the article titles in the HTML structure.
Scrape Article Details: For each article URL, the script scrapes the following:
Title: The headline of the article.
Description: A combined text extracted from paragraphs and list items within the article content.
Publication Date: The date the article was published.
Author: The name of the author.
Tags and Categories: Article metadata such as tags and categories for classification.
Save to CSV: Once the scraping is complete, the data is saved into a CSV file (wvua_news_data_communitystories_healthmatters_25.csv).
----------
Code Breakdown
Functions:
get_description(page_url): Extracts the description by scraping paragraphs (<p>) and list items (<li>) from the specified article page.
get_total_pages(base_url): Determines the total number of pages in the "Health Matters" section using pagination elements.
get_article_urls(page_url): Extracts article URLs from a given page by locating all the article title elements.
get_article_content(article_url): Scrapes detailed information from each article, including title, description, publication date, author, tags, and categories.
save_to_csv(data, filename): Saves the scraped data to a CSV file.
Main Script Flow:
The main() function orchestrates the entire process, starting with retrieving the total number of pages, then iterating through each page, scraping articles, and finally saving the results into a CSV file.
---------------

File Output
The CSV file will contain the following columns:

Title
URL
Description
Date Published
Author
Tags
Categories
Each row represents a scraped article with the respective information.
-----------------

Notes

Ensure your internet connection is stable since the script makes multiple HTTP requests.
The script handles dynamic content but may need adjustments if the website's HTML structure changes.
There are different categories in the website. Select a category first and then paste that link, then code download all the articles in that category, then change the link for other categories like sports, weather, and so on.
After scraping data create new coloumn as the Date that as been scraped.