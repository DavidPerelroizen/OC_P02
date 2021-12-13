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
    category_pages_url_list = []
    next_page_url_extract = 0
    indice = 0
    number_of_results_per_page = 20

    response_two = requests.get(url)
    soup_two = BeautifulSoup(response_two.text, features="html.parser")
    number_of_results_extract = soup_two.find('form').find('strong')
    number_of_results = int(number_of_results_extract.text)
    number_of_pages = math.ceil(number_of_results/number_of_results_per_page)

    if number_of_pages == 1:
        category_pages_url_list.append(url)

    else:
        for i in range(1, number_of_pages+1):
            category_pages_url_list.append(url[:52] + url[52:-11] + '/page-' + str(i) +'.html')

    return category_pages_url_list