from scrapy.contrib.loader.processor import MapCompose, Identity
from scrapy.contrib.loader import XPathItemLoader
from scrapy import log

from truScrape.items import projectItems


class RootItemLoader(XPathItemLoader):
    default_item_class = projectItems
    default_input_processor = Identity()
    default_ouput_processor = Identity()
