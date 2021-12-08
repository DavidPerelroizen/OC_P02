from bs4 import BeautifulSoup
import requests


def soupPage(url, html_element):
    """This function extracts a list of specified html_elements from a specified web page"""
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        element_list = soup.findAll(html_element)
        return element_list


