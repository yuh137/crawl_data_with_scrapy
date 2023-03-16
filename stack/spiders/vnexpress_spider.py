from scrapy import Selector
from scrapy import Spider


from stack.items import VNExpressItem

class YoutubeSpider(Spider):
    name = "vnexpress_items"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/the-gioi"
    ]

    def parse(self, response):
        articles = Selector(response).xpath("//*[@id='automation_TV0']/div/article")

        for article in articles:
            item = VNExpressItem()
            item['url'] = article.xpath("div/a/@href").extract()[0]
            item['title'] = article.xpath("h3/a/text()").extract()[0]
            item['description'] = article.xpath("p[@class='description']/a/text()").extract()[0]
            yield item