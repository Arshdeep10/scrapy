import scrapy

from ..items import HowjsayItem

# document.querySelectorAll('source[type="audio/mp3"]')[0].getAttribute('src')
class howjsay(scrapy.Spider):
    name = 'howjsay'
    start_urls = [
        'https://howjsay.com/b'
    ]
    
    def parse(self, response):
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