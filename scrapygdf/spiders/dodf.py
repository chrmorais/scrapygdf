# -*- coding: utf-8 -*-
import scrapy


class DodfSpider(scrapy.Spider):
    name = "dodf"
    allowed_domains = ["dodf.df.gov.br"]
    start_urls = (
        'http://www.dodf.df.gov.br/',
    )

    def parse(self, response):
        pass
