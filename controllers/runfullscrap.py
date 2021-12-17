from models.getcategoryurls import getproductcategories
from controllers.runcategoryscrap import categoryscrap
import os

"""
Function fullscrap :
------------------------
Step 1: get web site url
Step 2: get categories url list and names list
Step 3: scrap each category
------------------------
"""


def fullscrap(web_site_url, header):
    categories_to_scrap = getproductcategories(web_site_url)
    category_name = 0
    os.mkdir(r'C:\Users\david\PycharmProjects\Projets OC\P02\CSV_files')  # Create directory to store the CSV files
    os.mkdir(r'C:\Users\david\PycharmProjects\Projets OC\P02\Image_files')  # Create directory to store the Image files

    for category in categories_to_scrap:
        category_name = category[52:-11]
        categoryscrap(category, header, category_name)
