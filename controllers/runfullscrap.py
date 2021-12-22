from models.getcategoryurls import getproductcategories
from controllers.runcategoryscrap import categoryscrap
import os
import os.path
from models.constants import directory_image_files, directory_csv_files

"""
Function fullscrap :
------------------------
Step 1: get web site url
Step 2: get categories url list and names list
Step 3: scrap each category
------------------------
"""


def fullscrap(web_site_url, header):

    category_name = 0

    """
    While loop in order to check whether the directory name already exists and adapt the name if so
    Target is to avoid FileExistsError
    """
    i = 0
    csv_path = directory_csv_files
    while os.path.isdir(csv_path) == True:
        csv_path = csv_path + str(i)
        i += 1
    os.mkdir(csv_path)  # Create directory to store the CSV files

    """
    While loop in order to check whether the directory name already exists and adapt the name if so
    Target is to avoid FileExistsError
    """
    j = 0
    image_path = directory_image_files
    while os.path.isdir(image_path) == True:
        image_path = image_path + str(j)
        j += 1
    os.mkdir(image_path)  # Create directory to store the Image files

    categories_to_scrap = getproductcategories(web_site_url)

    for category in categories_to_scrap:
        category_name = category[52:-11]
        categoryscrap(category, header, category_name, csv_path, image_path)

