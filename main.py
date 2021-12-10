from models.webpage import url_site, url_page
from controllers.scrappage import *
from views.writepagecsv import *
from models.getcategoryurls import getproductcategories
from models.getnextpageslist import getnextpageslist
from models.getproductpageurllist import getproductpageurllist

url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/"

print(getproductpageurllist(url))

