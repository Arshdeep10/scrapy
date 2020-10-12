import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pprint import pprint

from ..items import ShabadkoshItem


class ShabadkoshSpider(scrapy.Spider):
    name = 'shabadkosh'
    start_urls = []
    alpha = 'W'
    for i in range(0, 4):
        start_urls.append(
            'https://www.shabdkosh.com/browse/english-hindi/' + alpha + '/1')
        alpha = chr(ord(alpha) + 1)

    def parse_audio_link(self, response, audio_name, full_link):
        items = ShabadkoshItem()
        id_list = response.xpath('//img[@class="audio"]/../@id').getall()
        print(id_list)
        items['audio_name'] = audio_name
        items['full_link'] = full_link
        items['pid1'], items['pid2'], items['pid3'], items['pid4'] = id_list
        yield items

    def parse(self, response, current_page_number=None):
        base_url = 'https://www.shabdkosh.com'
        word_page_links = response.css(
            'div.col-sm .mb-1::attr(href)').extract()
        for link in word_page_links:
            full_link = base_url + link
            audio_name = link.split('/')[-2]
            extra_args = {'audio_name': audio_name, 'full_link': full_link}
            yield response.follow(full_link, callback=self.parse_audio_link, cb_kwargs=extra_args)

        next_page_number = response.request._cb_kwargs.get(
            'current_page_number', 1) + 1
        next_page = response._url.rsplit('/', 1)[0]
        next_page = next_page + "/" + str(next_page_number)
        if len(word_page_links) != 0:
            print("url = ", next_page, ", page_number = ", next_page_number)
            extra_args = {'current_page_number': next_page_number}
            yield response.follow(next_page, cb_kwargs=extra_args, callback=self.parse)
