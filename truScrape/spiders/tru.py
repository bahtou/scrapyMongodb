from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from scrapy import log

from truScrape.loaders import RootItemLoader


def saveIt(body):
    html = open('../webpage.html', 'w')
    html.write(body)
    html.close()
    pass


class truSpider(BaseSpider):
    name = 'tru'
    allowed_domains = ['truonex.com']
    start_urls = ['http://www.truonex.com/']

    def parse(self, response):
        log.msg('login', level=log.INFO)
        return [FormRequest.from_response(response,
                formdata={'user_email': 'Username@email.com', 'user_password': 'UserPassword'},
                callback=self.after_login)]

    def after_login(self, response):
        log.msg('loged in!!', level=log.INFO)
        saveIt(response.body)

        loader = RootItemLoader(response=response)

        loader.add_xpath('url', response.url)
        loader.add_xpath('title', "//h3[@class='project_title']/a/text()")
        loader.add_xpath('org', )
        loader.add_xpath('author', )
        loader.add_xpath('updated', "//div[@class='span2 updated_at']/text()")
        loader.add_xpath('summary', )
