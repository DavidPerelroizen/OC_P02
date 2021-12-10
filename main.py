from models.webpage import url_site, url_page
from controllers.scrappage import *
from views.writepagecsv import *
from models.getcategoryurls import getproductcategories
from models.getnextpageslist import getnextpageslist
from models.getproductpageurllist import getproductpageurllist
from controllers.runcategoryscrap import categoryscrap

url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/"

print(len(categoryscrap(url)))

