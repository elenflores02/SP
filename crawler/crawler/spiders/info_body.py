import scrapy

class info_body(scrapy.Spider):
    name = "body"
    allowed_domains = ["sunstar.com.ph"]

    start_urls = []

    for line in open('links.txt'):
        start_urls.append(line.strip('\r\n'))

    def parse(self, response):
        filename = "html-files/" + response.url.split("-")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

#scrapy crawl body
