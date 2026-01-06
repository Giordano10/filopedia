from crawler.scrapers.spiders.wikipedia import WikipediaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl(WikipediaSpider)
process.start()