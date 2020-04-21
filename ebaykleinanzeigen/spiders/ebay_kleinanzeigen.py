# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy
import ebaykleinanzeigen.spiders.article_database as article_database

from ebaykleinanzeigen.spiders.utilities import Utilities

directory_path = "C:/Users/MaxMustermann/Desktop/Ebay/Pictures/"
#  path to the directory where the pictures should be saved

min_number_pictures = 4  # only downloads pictures if more than min_number_pictures are available

scrape_next_pages = True  # scrape more than the first page?


class EbayKleinanzeigenSpider(scrapy.Spider):
    name = 'ebay_kleinanzeigen'
    allowed_domains = ['ebay-kleinanzeigen.de']

    def __init__(self, *args, **kwargs):
        # Load home made classes with functions
        self.utilities = Utilities()

        # Load of configuration files
        self.start_urls = self.utilities.load_urls("urls.json")

        self.unique_identifier = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
        self.counter = 0

    def parse(self, response):
        article_urls = response.xpath("//a[@class='ellipsis']/@href").extract()
        for url in article_urls:
            domain = 'https://www.ebay-kleinanzeigen.de'
            article_page = response.urljoin(domain + url)
            request = scrapy.Request(url=article_page, callback=self.parse_article_page, dont_filter=True)
            yield request

        next_page = domain + str(response.xpath("//a[@class='pagination-next']/@href").extract_first())
        if next_page is not None and scrape_next_pages:  # If still some next pages to follow and if it's allowed
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_article_page(self, response):

        article_number = response.xpath("//input[@name='adId']").attrib["value"]

        if article_database.check_article_number(article_number):
            return

        article_details_categories = [s.replace(":", "") for s in
                                      response.xpath("//li[@class='addetailslist--detail']//text()").extract()]
        index = 0
        article_brand = ""
        article_model = ""
        while index < len(article_details_categories):
            article_details_categories[index] = article_details_categories[index].strip()
            if article_details_categories[index] == "Marke":
                article_brand = article_details_categories[index + 1].strip()
            if article_details_categories[index] == "Modell":
                article_model = article_details_categories[index + 1].strip()
            index += 1

        article_images = response.xpath("//div[@class='galleryimage-large l-container-row j-gallery-image']").css(
            'img').xpath('@src').getall()
        if len(article_images) > min_number_pictures:
            if not article_brand:
                article_folder_path = directory_path + "No Brand"
            else:
                article_folder_path = directory_path + article_brand

            self.utilities.create_folder(article_folder_path)
            image_counter = 0
            for image in article_images:
                image_path = article_folder_path + "/" + self.unique_identifier + " " + article_brand + " " + \
                             article_model + " " + str(self.counter) + "_" + str(image_counter) + ".jpg"
                self.utilities.save_image(image, image_path)
                image_counter += 1

            article_database.save_article(article_database.create_article_json(article_number,
                                                                               self.unique_identifier, article_images))

        self.counter += 1
