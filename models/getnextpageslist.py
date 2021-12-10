import requests
from bs4 import BeautifulSoup
import math

def getnextpageslist(url):
    """
    From a given book category first page, extract all the URLs of the pages associated to this category
    Return a list
    :param url:
    :return:
    """
    category_pages_url_list = [url]
    next_page_url_extract = 0
    indice = 0
    number_of_results_per_page = 20

    response_two = requests.get(url)
    soup_two = BeautifulSoup(response_two.text, features="html.parser")
    number_of_results_extract = soup_two.find('form').find('strong')
    number_of_results = int(number_of_results_extract.text)
    number_of_pages = math.ceil(number_of_results/number_of_results_per_page)

    for i in range(0, number_of_pages-1):
        response = requests.get(category_pages_url_list[indice])
        if response.ok:
            soup = BeautifulSoup(response.text, features="html.parser")
            next_page_url_extract = soup.find('li', 'next').find('a')
            next_page_url = next_page_url_extract['href']
            category_pages_url_list.append(str(url) + next_page_url)
            indice += 1

    return category_pages_url_list