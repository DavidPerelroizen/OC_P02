from bs4 import BeautifulSoup
import requests


def soupPage(url, html_element):
    """This function extracts a list of specified html_elements from a specified web page and returns that list"""
    response = requests.get(url)
    if response.ok:
        element_list = []
        soup = BeautifulSoup(response.text, features="html.parser")
        element_extract = soup.findAll(html_element)
        for i in element_extract:
            element_list.append(i.text)
        return element_list



