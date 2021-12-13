from views.writepagecsv import csv_header
from controllers.runfullscrap import fullscrap

url_category = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
url_website = "https://books.toscrape.com"
url_product_page = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'


fullscrap(url_website, csv_header)


