from views.writepagecsv import csv_header
from controllers.runfullscrap import fullscrap

url_website = "https://books.toscrape.com"

fullscrap(url_website, csv_header)


