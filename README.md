# Web Scrapers
### Author: Dylan Mendonca

This repository contains a few web scrapers I built primarily using Python's `requests` and `bs4` libraries.

There are two scrapers:
1. `bookstore_webscraper.py`: This file contains functions that help scrape book information from [this](http://books.toscrape.com/catalogue/) website.
2. `nasdaq_webscraper.py`: This file contains functions that help scrape stock data from [this](https://www.nasdaq.com/screening/companies-by-industry.aspx) NASDAQ webpage.

## Sample Usage for Each File:
### `bookstore_webscraper.py`
To scrape data from pages 1 to 3, run the following command. The output of this function is a pandas dataframe
> data = bookstore_scraper('http://books.toscrape.com/catalogue/',1,3)

### `nasdaq_webscraper.py`
To scrape data from pages 1 to 10, run the following command. The output of this function is a nested dictionary of the form:
> {'Company_Name': [{'Symbol': 'XXX',
>   'Current_Market_Cap': 'YYY',
>   'Country': 'ZZZ',
>   'IPO_Year': 'AAA',
>   'Subsector': 'BBB'}],.....}

> urls = generate_url('https://www.nasdaq.com/screening/companies-by-industry.aspx',10)
> companies = get_financial_data(urls)

