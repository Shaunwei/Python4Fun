from scrapy.spider import Spider
from scrapy.selector import Selector
import re

class DmozSpider( Spider ):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        for site in sites:
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('text()').extract()
            #title = clean_data(title)
            #link = clean_data(link)
            #desc = clean_data(desc)
            print "title: ",title
            print "link: ",link
            print "desc: ",desc
        
def clean_data(data):
    cleaned_data = re.sub(r'[\n\r\t]','', data)
    return cleaned_data
