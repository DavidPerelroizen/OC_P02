import requests
from bs4 import BeautifulSoup

def getproductcategories(url):
    """
    From a the website url, extract all the books categories urls and store them in a list
    Return that list
    """
    product_categories_url_list = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        categories_url_extract = soup.find('aside').findAll('a')
        for a in categories_url_extract:
            item = a['href']
            product_categories_url_list.append("https://books.toscrape.com/"+item)
        product_categories_url_list.pop(0)
    return product_categories_url_list
