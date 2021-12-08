from bs4 import BeautifulSoup, NavigableString
import requests


def scrapPage(url):
    """This function extracts the list of the wanted from a specified web page and returns that list"""
    response = requests.get(url)
    if response.ok:
        element_list = [url]
        soup = BeautifulSoup(response.text, features="html.parser")

        """Extract the TD elements and add the right ones to the element_list"""
        element_extract = soup.findAll('td')
        for i in element_extract:
            element_list.append(i.text)
        element_list.pop(2)
        element_list.pop(4)
        element_list.pop(5)

        """Extract the title and add it to the element_list"""
        title_extract = soup.find('h1')
        title_clean = title_extract.text
        element_list.insert(2, title_clean)

        """Extract the product description and add it to the element_list"""
        product_description_extract = soup.findAll("p")
        element_list.append(product_description_extract[3].text)

        """Extract the product category and add it to the element_list"""
        product_category_extract = soup.findAll('a')
        element_list.append(product_category_extract[3].text)

        """Extract review rating and add it to the element_list"""



        return element_list




