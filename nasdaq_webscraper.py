# Importing necessary modules
import requests
from bs4 import BeautifulSoup

'''
This function is used to generate a URL for the different pages in the NASDAQ website. 
The function starts at 1 and goes up to the page you give it (the NASDAQ website has
138 pages in total).
'''
def generate_url(base,pages):
    urls = []
    for i in range(1,pages+1):
        if i == 1:
            urls.append(base)
        else:
            urls.append(base + '?page=' + str(i))
    return urls


'''
This function takes a URL, extracts the HTML from that URL and then stores the important stock data
(name, stock symbol, etc.) into a dictionary which it outputs
'''
def get_financial_data(urls):
    company_dict = {}
    for url in urls:
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        table_company = soup.find('table',id = 'CompanylistResults')
        for row in table_company.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) == 0 or len(cells) == 1:
                continue
            name = cells[0].string
            company_dict[name] = [{'Symbol': cells[1].find('a').string.strip(),'Current_Market_Cap': cells[2].string, 'Country': cells[4].string, 'IPO_Year': cells[5].string, 'Subsector': cells[6].string}] 
    return company_dict