from models.getnextpageslist import getnextpageslist
from models.getproductpageurllist import getproductpageurllist
from views.writepagecsv import writeCsvFile

def categoryscrap(url_category, header, book_category_name, csv_directory_path, image_directory_path):
    """
    Step 1: get category page url --> in function arguments
    Step 2: get the list of all pages from this category
    Step 3: for each page from Step 2 list, get the list of all the products pages url
    Step 4: combine the products pages url lists of each page into one list of urls
    Step 5: create a csv file for all the category products
    """

    next_pages_list = getnextpageslist(url_category)  # Step 2
    product_pages_url_list = []

    # Code block below combines steps 3 & 4
    for page in next_pages_list:
        for i in getproductpageurllist(page):
            product_pages_url_list.append(i)

    # Step 5
    return writeCsvFile(header, book_category_name, product_pages_url_list, csv_directory_path, image_directory_path)
