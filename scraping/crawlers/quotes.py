from scraping.crawler_base import Crawler

from models.quotes import Quotes as QuotesModel

from scraping import logger
from typing import Dict


class Quotes(Crawler):
    """ Crawler Quotes
    """
    
    def __init__(self, config: Dict):
        super().__init__(
            crawler_name=config.get('crawler_name', 'quotes'),
            url=config.get('url'),
            model_item=QuotesModel
        )
        self.config = config
        
    def execute(self) -> None:
        # executar request na página
        self.request()
        
        quotes = self.response.select(self.config.get('class_quote'))
        logger.info(f"total items - {len(quotes)}")
        
        for quote in quotes:
            try:
                item = {
                    'text': quote.select_one(self.config.get('class_text')).text,
                    'by': quote.select_one(self.config.get('class_author')).text,
                    'tags': quote.select_one(self.config.get('class_keywords')).get('content')
                }
                
                self.items.append(item)
                logger.info(f"item - {item}")
            except:
                logger.error(f"fails to extract item")
        
        # salvar dados extraidos
        self.save()