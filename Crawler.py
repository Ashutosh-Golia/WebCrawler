from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings=get_project_settings()
settings["FEEDS"] = {"author.json": {"format": "json", "overwrite": "True"}}

process = CrawlerProcess(settings=settings)

process.crawl("author")
process.start()  # the script will block here until the crawling is finished