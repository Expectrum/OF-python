# Python Web Scraping Script Explanation

This script is a Python program designed to scrape data from a specific website, extract relevant information, and save it in a JSON file. Below is a detailed breakdown of the script:

## Script Overview

The script performs the following tasks:
1. **Fetches HTML content** from a specified URL.
2. **Parses the HTML** to extract specific data.
3. **Navigates through multiple pages** to gather detailed information.
4. **Stores the collected data** in a structured JSON file.

## Dependencies

The script uses the following Python libraries:
- `requests`: To make HTTP requests and fetch web content.
- `BeautifulSoup` from `bs4`: To parse HTML and extract data.
- `urljoin` from `urllib.parse`: To construct full URLs from relative paths.
- `json`: To handle JSON data and save it to a file.
