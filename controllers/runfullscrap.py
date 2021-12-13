from models.getcategoryurls import getproductcategories
from controllers.runcategoryscrap import categoryscrap
"""
Step 1: get web site url
Step 2: get categories url list and names list
Step 3: scrap each category
"""

def fullscrap(web_site_url, header):

    categories_to_scrap = getproductcategories(web_site_url)
    category_name = 0
    for category in categories_to_scrap:
        category_name = category[52:-11]
        categoryscrap(category, header, category_name)
