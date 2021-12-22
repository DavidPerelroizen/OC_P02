from controllers.scrappage import scrapPage
import csv

csv_header = [
    "product_page_url",
    "universal_product_code (upc)",
    "title",
    "price_including_tax",
    "price_excluding_tax",
    "number_available",
    "product_description",
    "category",
    "review_rating",
    "image_url"
]


def writeCsvFile(header, output_file_name, pages, csv_folder_path, image_folder_path):
    """Create a CSV file where it will write the result of the page scrapping for a given list of pages"""
    with open(csv_folder_path + "/" + str(output_file_name) + '.csv', 'w', encoding='utf-8') as outf:
        writer = csv.writer(outf)
        writer.writerow(header)
        for page in pages:
            scrapping_result = scrapPage(page, image_folder_path)
            writer.writerow(scrapping_result)
        return outf

