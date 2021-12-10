from models.getnextpageslist import getnextpageslist
from models.getproductpageurllist import getproductpageurllist
"""
Step 1: get category page url
Step 2: get the list of all pages from this category
Step 3: for each page from Step 2 list, get the list of all the products pages url
Step 4: combine the products pages url lists of each page into one list of urls
Step 5: create a csv file for all the category products
"""

def categoryscrap(url_category):

    next_pages_list = getnextpageslist(url_category)
    product_pages_url_list = []

    for page in next_pages_list:
        temp_list = getproductpageurllist(page)
        for i in temp_list:
            product_pages_url_list.append(i)

