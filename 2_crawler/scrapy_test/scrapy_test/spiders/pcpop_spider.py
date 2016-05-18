import bs4
from bs4 import BeautifulSoup
from scrapy.spider import Spider
from scrapy import Request

class DmozSpider(Spider):
    name = "pcpop"
    allowed_domains = ["pcpop.com"]
    start_urls = [
        "http://pop.pcpop.com/"
        ]

    def parse(self, response):
        filename = "./crawl_result/" + response.url.split("/")[-2]
        open(filename, "wb").write(response.body)

        soup = BeautifulSoup(response.body)
        if not (soup == None or soup.body == None):
            for c in soup.body.descendants:
                if isinstance(c, bs4.element.NavigableString):
                    continue
                if "href" in c.attrs:
                    if c.attrs["href"].find("pcpop.com") != -1:
                        url = c.attrs["href"]
                        yield Request(url, callback=self.parse)
