from bs4 import BeautifulSoup
import requests
import shutil
import string
from models.constants import FORBIDDEN_CHARACTERS_IN_FILES


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
        paragraphs_extract = soup.findAll('p')
        review_rating_extract = paragraphs_extract[2]
        review_rating = review_rating_extract['class']
        element_list.append(review_rating[1])


        """Extract image url and add it to the element_list"""
        image_url_extract = soup.find('img')
        image_url = image_url_extract['src']
        image_url = 'https://books.toscrape.com' + image_url[5:]
        element_list.append(image_url)

        """Download and save the image file"""
        req_img = requests.get(image_url, stream=True)
        for c in FORBIDDEN_CHARACTERS_IN_FILES:  # avoids trouble when saving the image file
            title_clean = title_clean.replace(c, '')
        if req_img.status_code == 200:
            with open(r'C:\Users\david\PycharmProjects\Projets OC\P02\Image_files' + '\\' + title_clean + image_url[-4:], 'wb') as f:
                shutil.copyfileobj(req_img.raw, f)
        
        return element_list



