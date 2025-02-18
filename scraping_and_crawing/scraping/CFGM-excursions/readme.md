# Web Scraping for Excursion Data: Python Script

## Overview

This Python script is designed to scrape excursion data from a website dedicated to educational programs. The script extracts information related to educational modules and the excursions associated with each program. The final data is stored in a structured JSON file, making it easy to analyze or share.

### Libraries Used:

- **requests**: This library is used for sending HTTP requests to retrieve the HTML content of the web pages.
- **BeautifulSoup** (from `bs4`): This library helps parse and navigate through the HTML content, allowing us to extract specific elements such as links, text, and attributes.
- **urljoin** (from `urllib.parse`): It ensures that the URLs scraped are absolute by converting relative URLs to fully qualified URLs.
- **json**: This library is used to save the scraped data in a JSON format, making it easy to process later.

---

## Script Breakdown

### 1. **Import Libraries**
The script starts by importing necessary libraries:

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
```
