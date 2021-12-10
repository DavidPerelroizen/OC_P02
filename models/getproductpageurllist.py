import requests
from bs4 import BeautifulSoup

def getproductpageurllist(url):
    """
    Scrap the a page displaying several books and get each product page url
    :param url:
    :return: list of url
    """
    product_page_url_list = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        product_page_url_extract = soup.find('ol', 'row').findAll('a')
        for i in product_page_url_extract:
            item = i['href']
            item_clean = item[9:]
            product_page_url_list.append("https://books.toscrape.com/catalogue/" + item_clean)

        return product_page_url_list
