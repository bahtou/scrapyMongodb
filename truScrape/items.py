from scrapy.item import Item, Field
from scrapy import log


class projectItems(Item):
    log.msg('loading item containers', level=log.INFO)
    title = Field()     # //h1[class='view_project_title']/text()
    org = Field()       # //div[@class='span4 organization']/h4/a/text()
    author = Field()    # //div[@class='span4 user_full_name']/h4/text()
    updated = Field()   # //div[@class='span4 created_at']/h4/text()
    summary = Field()   # //div[@class='row project_descript']/div/text()
    url = Field()
    pass
