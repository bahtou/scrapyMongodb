# Scrapy settings for truScrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'truScrape'

SPIDER_MODULES = ['truScrape.spiders']
NEWSPIDER_MODULE = 'truScrape.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Opera/9.80 (J2ME/MIDP; Opera Mini/6.1.25378/25.692; U; en) Presto/2.5.25 Version/10.54'

DOWNLOAD_DELAY = 2

PATH_DEBUG = True
PATH_DEBUG_URL_LENGTH = 97

ITEM_PIPELINES = ['truScrape.pipelines.mongodbPipeline']

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "truonex"
MONGODB_COLLECTION = "projects"

# Maximum number of concurrent items (per response) to process in parallel in the Item Processor (also known as the Item Pipeline).
CONCURRENT_ITEMS = 100

# The maximum number of concurrent (ie. simultaneous) requests that will be performed by the Scrapy downloader.
# The maximum number of requests that the request_container can fill-up.  The container is filled to capacity with the requests.  Then as one exits, another fills its spot.  When there are no more requests to fill a vacancy, the container simply empties.
# This effect is most noticibly when 'Closing spider (shutdown)'
CONCURRENT_REQUESTS = 8

# The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single domain.
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single IP. If non-zero, the CONCURRENT_REQUESTS_PER_DOMAIN setting is ignored, and this one is used instead. In other words, concurrency limits will be applied per IP, not per domain
CONCURRENT_REQUESTS_PER_IP = 0

DOWNLOADER_STATS = True
RANDOMIZE_DOWNLOAD_DELAY = True
