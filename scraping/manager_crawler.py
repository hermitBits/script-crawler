from typing import List

from scraping import logger
from scraping.crawler_base import CrawlerBase


class ManagerCrawler:
    """ Classe gerencia execução dos crawlers
    """
    
    def __init__(self) -> None:
        self.crawlers : List[CrawlerBase] = []

    def add_crawler(self, crawler: CrawlerBase) -> None:
        """ Empilhar crawlers
        
        Args:
            crawler: recebe um crawler
        """
        self.crawlers.append(crawler)
        logger.info(f"added crawler - {crawler.crawler_name}")

    
    def execute_crawlers(self) -> None:
        for crawler in self.crawlers:
            try:
                logger.info(f"running - {crawler.crawler_name} crawler")
                crawler.execute()
            except Exception as e:
                logger.error(f'error in executing - {crawler.crawler_name} - {e}')
