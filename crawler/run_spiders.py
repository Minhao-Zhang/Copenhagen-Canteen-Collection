import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.foodco_ku_frederiksberg import KUFrederiksbergCampusCanteen
from spiders.foodco_ku_north import KUNorthCampusCanteen
from spiders.foodco_ku_south import KUSouthCampusCanteen
from spiders.foodco_ku_geocentercity import KUGeoCenterCampusCityCanteen
from spiders.foodco_ku_taastrup import KUTaastrupCampusCanteen

DATA_PATH = "../../data/"

process = CrawlerProcess()
process.crawl(KUFrederiksbergCampusCanteen)
process.crawl(KUNorthCampusCanteen)
process.crawl(KUSouthCampusCanteen)
process.crawl(KUGeoCenterCampusCityCanteen)
process.crawl(KUTaastrupCampusCanteen)
process.start()
