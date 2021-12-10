from models.webpage import url_site, url_page
from controllers.scrappage import *
from views.writepagecsv import *
from models.getcategoryurls import getproductcategories

url = url_site

print(getproductcategories(url))

