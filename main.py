from models.webpage import url_site, url_page
from controllers.scrappage import *
from views.writepagecsv import csv_header
from models.getcategoryurls import getproductcategories
from models.getnextpageslist import getnextpageslist
from models.getproductpageurllist import getproductpageurllist
from controllers.runcategoryscrap import categoryscrap

url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/"

categoryscrap(url, csv_header, 'Sequential_art')

