import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.foodco_ku_north import KUNorthCampusCanteen


DATA_PATH = "../../data/"

# get north campus 
process = CrawlerProcess()
process.crawl(KUNorthCampusCanteen)
process.start()
