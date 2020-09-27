import scrapy

from ..items import HowjsayItem


class howjsay(scrapy.Spider):
    name = 'howjsay'
    start_url = [
        'https://howjsay.com/b?page=2'
    ]

    def parse(self, response):
        audio_link = response.css('source[type="audio/mp3"]')
        print(audio_link)
        # url = scrapy.Request(url, callback = self.parse2)
        # yield url
