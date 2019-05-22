# Importing necessary modules
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from pandas import DataFrame


#######################
#### MAIN FUNCTION ####
#######################

'''
This is the main function. You provide it with the base url for the website (http://books.toscrape.com/catalogue/ in this case).
and the page numbers you'd like to scrape from the website. It returns the scraped data in the form of a Pandas DataFrame
'''
def bookstore_scraper(base,*pages):
    dataframe = defaultdict(list)
    for page in range(pages[0],pages[1]+1):
        url = generate_url(base,page)
        data = connect_to_page(url)
        rating_list,header_list,price_list,in_stock_list = scrape_page(data)
        dataframe['rating_out_of_5'].extend(rating_list)
        dataframe['name'].extend(header_list)
        dataframe['price'].extend(price_list)
        dataframe['in_stock'].extend(in_stock_list)
    return DataFrame(dataframe)



########################
### HELPER FUNCTIONS ###
########################    

'''
This function appends /page-(page_number).html to the base url.
Eg: generate_url('www.hello.com/',1) gives 'www.hello.com/page-1.html'
'''
def generate_url(base,page_number):
    return base + f'page-{page_number}.html'


'''
This function requests a url for its HTML and returns the HTML content from the url
'''
def connect_to_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.content)


'''
This function takes HTML content as input "page" and returns 4 lists of data (ratings,
name, price, in stock)
'''
def scrape_page(page):
    main_stuff = page.findAll('ol')
    rating_list = []
    header_list = []
    price_list = []
    in_stock_list = []
    for ele in main_stuff:
        for li in ele.findAll('li'):
            rating = li.find('p', {'class':'star-rating'})['class'][1]
            rating_list.append(rating)
            header = li.findAll('a')[1]['title']
            header_list.append(header)
            price = li.find('p',{'class':'price_color'}).text
            price_list.append(price)
            in_stock = li.find('p',{'class':'instock availability'}).text.strip()
            in_stock_list.append(in_stock)
    return rating_list,header_list,price_list,in_stock_list  