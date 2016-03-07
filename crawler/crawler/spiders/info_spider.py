import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from crawler.items import CrawlerItem

class InfoSpider(scrapy.Spider):
    name = "info"
    allowed_domains = ["sunstar.com.ph"]
    start_urls = [
        "http://www.sunstar.com.ph/latest-news/"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items", follow= True),
    )

    #def parse(self, response):
    #    filename = response.url.split("/")[-2] + '.html'
    #    with open(filename, 'wb') as f:
    #        f.write(response.body)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath('//span[@class="more"]')
        items = []
        for titles in titles:
            item = CrawlerItem()
            item["title"] = titles.xpath("a/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            items.append(item)
        return(items)