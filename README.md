DgPad-Data-Science-2024:
This task is designed to scrape articles from a website using its sitemap. It involves fetching and parsing the sitemap, extracting article URLs, 
downloading and parsing article content, and finally saving the extracted data in JSON format. 
Process & Goal:
The process involves several steps including sitemap parsing, article scraping, and data saving... 
The goal is to collect article data and save it in a structured format for further analysis or use.
Below is a detailed overview of the structure and functionality of the project.
Data Structure:
      !using the following data structure to hold article details:
from dataclasses import dataclass

@dataclass
class Article:
    url: str
    title: str
    keywords: list
    author: str
    date: str
    content: str
The SitemapParser class handles the extraction of URLs from the website's sitemap.
The ArticleScraper class is responsible for downloading and parsing the HTML content of each article.
The FileUtility class manages the creation of directories and saving of the extracted articles in JSON format.
THENRunning the Script 
Installation

    main_sitemap_url = "https://www.almayadeen.net/sitemaps/all.xml"

home = C:\Users\V15 G2\AppData\Local\Programs\Python\Python312
implementation = CPython
version_info = 3.12.5.final.0
virtualenv = 20.24.5
include-system-site-packages = false
base-prefix = C:\Users\V15 G2\AppData\Local\Programs\Python\Python312
base-exec-prefix = C:\Users\V15 G2\AppData\Local\Programs\Python\Python312
base-executable = C:\Users\V15 G2\AppData\Local\Programs\Python\Python312\python.exe
