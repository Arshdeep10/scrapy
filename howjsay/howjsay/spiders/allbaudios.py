import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import HowjsayItem

class AllbaudiosSpider(CrawlSpider):
    name = 'allbaudios'
    allowed_domains = ['howjsay.com']
    start_urls = ['https://howjsay.com/b']

    rules = (
        Rule(LinkExtractor(attrs=(src)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        audio_link = response.css('source[type="audio/mp3"]::attr(src)').extract()
        print(audio_link)
        string = 'https://howjsay.com/'
        items = HowjsayItem()
        links = []
        for i in audio_link:
            url = string + i
            print(url)
            # url = scrapy.Request(url)
            links.append(url)
        items['file_urls'] = links
        yield items
        
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
