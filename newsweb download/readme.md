# Project Overview
This Python script is designed to scrape articles from all sections of the WVUA23 website. The script extracts information such as the article title, description, publication date, author, tags, and categories from multiple pages and saves the data in a CSV file.

Features
------------
Scrapes multiple pages of articles automatically.
Extracts title, description, publication date, author, tags, and categories for each article.
Combines content from paragraphs and list items into a single description.
Saves the collected data into a CSV file for further analysis.
Requirements
To run this script, you will need the following Python libraries installed:
requests: To make HTTP requests to the website.
beautifulsoup4: For parsing the HTML content.
pandas: To store and manipulate the scraped data in a CSV file.

How It Works
------------
Scrape Pagination: The script first determines the total number of pages by analyzing the pagination element on the website.
Extract Article URLs: For each page, the script retrieves all article URLs by locating the article titles in the HTML structure.
Scrape Article Details: For each article URL, the script scrapes the following:
Title: The headline of the article.
Description: A combined text extracted from paragraphs and list items within the article content.
Publication Date: The date the article was published.
Author: The name of the author.
Tags and Categories: Article metadata such as tags and categories for classification.
Save to CSV: Once the scraping is complete, the data is saved into a CSV file (wvua_news_data_communitystories_healthmatters_25.csv).


File Output
------------
The CSV file will contain the following columns:

Title
URL
Description
Date Published
Author
Tags
Categories
Each row represents a scraped article with the respective information.

Notes
------------
Please make sure your internet connection is stable since the script makes multiple HTTP requests.
The script handles dynamic content but may need adjustments if the website's HTML structure changes.
The website has different categories. First, select a category and paste that link. Then, the code downloads all the articles in that category. Then, change the link for other categories like sports, weather, and so on.
After scraping data create a new column as the Date that has been scraped.
