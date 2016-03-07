import scrapy

class info_body(scrapy.Spider):
    name = "body"
    allowed_domains = ["sunstar.com.ph"]
    start_urls = [
        "http://www.sunstar.com.ph/manila/local-news/2016/03/07/american-tests-positive-zika-virus-while-philippines-461056",
        "http://www.sunstar.com.ph/cebu/local-news/2016/03/06/poe-escudero-trekking-votes-461029",
        "http://www.sunstar.com.ph/manila/local-news/2016/03/05/philippines-impounds-north-korean-ship-460912",
        "http://www.sunstar.com.ph/manila/local-news/2016/03/04/sos-diliman-holds-world-premiere-music-video-lumad-460720",
        "http://www.sunstar.com.ph/baguio/local-news/2016/03/03/farm-ads-banned-benguet-460565",
        "http://www.sunstar.com.ph/network/local-news/2016/03/03/indonesia-lifts-tsunami-alert-issued-after-powerful-quake-460458",
        "http://www.sunstar.com.ph/manila/local-news/2016/02/29/npc-formally-endorses-poe-escudero-tandem-459880",
        "http://www.sunstar.com.ph/baguio/local-news/2016/02/27/baguio-roads-closed-2-day-grand-parade-459561"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)