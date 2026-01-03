from crawler.constants import DATA_PATH, URL_AUX

DATA_PATH = DATA_PATH
URL_AUX = URL_AUX

from crawler.scrapers.items import WikipediaItem
from crawler.scrapers.spiders.wikipedia import WikipediaSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())
process.crawl(WikipediaSpider)
process.start()