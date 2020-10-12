import scrapy
import csv
from ..items import DshabadkoshItem


class DshabadkoshSpider(scrapy.Spider):
    name = 'dshabadkosh'
    base_url = 'https://www.shabdkosh.com/speech/sayit.php?x=mp3&v=3&id='
    start_urls = [
        'https://www.shabdkosh.com/dictionary/english-hindi/aa/aa-meaning-in-hindi']

    def parse(self, response):
        csvfile = open('shabadkosh.csv', 'r')
        csv_reader = csv.DictReader(csvfile)
        items = DshabadkoshItem()
        filenames = []
        links = []
        for row in csv_reader:
            id_link1 = self.base_url + row['pid1']
            id_link2 = self.base_url + row['pid2']
            id_link3 = self.base_url + row['pid3']
            id_link4 = self.base_url + row['pid4']
            print(id_link1, id_link2, id_link3, id_link4)
            links.append(id_link1)
            links.append(id_link2)
            links.append(id_link3)
            links.append(id_link4)
            filenames.append(row['audio_name'] + "_pid1")
            filenames.append(row['audio_name'] + "_pid2")
            filenames.append(row['audio_name'] + "_pid3")
            filenames.append(row['audio_name'] + "_pid4")
        items['file_names'] = filenames
        items['file_urls'] = links
        yield items
