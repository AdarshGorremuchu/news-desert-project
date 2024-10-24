# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:30:33 2024

@author: ADARSH G
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get the description from the HTML of the webpage
def get_description(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the section containing the paragraphs
    meta_details = soup.find('div', class_='basic-content-wrap cf')
    
    # Check if the section is found
    if not meta_details:
        print("meta-details not found.")
        return "Description not found."
    
    # Extract text from all <p> tags within the section
    description_paragraphs = meta_details.find_all('p')
    description_texts = [para.get_text(strip=True) for para in description_paragraphs]

    # Extract text from all <li> tags within <ul> elements
    ul_elements = meta_details.find_all('ul')
    list_items_texts = []
    for ul in ul_elements:
        list_items = ul.find_all('li')
        list_items_texts.extend([li.get_text(strip=True) for li in list_items])

    # Combine <p> and <li> texts
    description = ' '.join(description_texts + list_items_texts)
    
    return description

# Function to get the total number of pages
def get_total_pages(base_url):
    response = requests.get(base_url + '1/')
    soup = BeautifulSoup(response.content, 'html.parser')
    pagination = soup.find('nav', class_='pagination')
    total_pages = int(pagination.find_all('a', class_='page-numbers')[-2].text)
    return total_pages

# Function to get all article URLs from a page
def get_article_urls(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h3', class_='entry-title')
    urls = [article.find('a')['href'] for article in articles]
    return urls

# Function to get content from a specific article URL
def get_article_content(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Heading
    title_tag = soup.find('h1', class_='entry-title')
    title = title_tag.get_text() if title_tag else 'N/A'
    
    # Description using the updated get_description function
    description = get_description(article_url)
    
    # Author and date published
    date_tag = soup.find('time', class_='updated entry-time')
    date_published = date_tag.get_text() if date_tag else 'N/A'
    
    author_tag = soup.find('div', class_='entry-author')
    author = author_tag.get_text(strip=True) if author_tag else 'N/A'
    
    # Tags
    tag_div = soup.find('div', class_='article-tags')
    tags = [tag.get_text() for tag in tag_div.find_all('a')] if tag_div else []
    
    # Categories
    category_div = soup.find('div', class_='article-categories')
    categories = [category.get_text() for category in category_div.find_all('a')] if category_div else []
    
    article_data = {
        'Title': title,
        'URL': article_url,
        'Description': description,
        'Date Published': date_published,
        'Author': author,
        'Tags': ', '.join(tags),
        'Categories': ', '.join(categories)
    }
    
    return article_data

# Function to save data to a CSV file
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data has been saved to {filename}")

# Main function to scrape all pages and articles
def main():
    base_url = 'https://www.wvua23.com/communitystories/healthmatters/'
    total_pages = get_total_pages(base_url)
    all_news_data = []
    
    for page_num in range(1, total_pages + 1):
        page_url = base_url + str(page_num) + '/'
        print(f"Scraping page {page_num} of {total_pages}")
        article_urls = get_article_urls(page_url)
        for article_url in article_urls:
            print(f"Scraping article: {article_url}")
            article_data = get_article_content(article_url)
            all_news_data.append(article_data)
    
    save_to_csv(all_news_data, 'wvua_news_data_communitystories_healthmatters_25.csv')

if __name__ == '__main__':
    main()
