import json
import requests
import os
import uuid


from datetime import datetime
from abc import abstractmethod
from bs4 import BeautifulSoup

from database.db_sqlite import session

from scraping import logger


class CrawlerBase():
    """ Classe para base de um crawler
    """
    
    def __init__(self, crawler_name, url, model_item):
        self.url = url
        self.crawler_name = crawler_name
        self.items = []
        self.model_item = model_item
        self.batch = None
        self.response = None
        
    def request(self) -> None:
        """ executar request na página que será feita raspagem
        """
        
        try:
            r = requests.get(self.url)
            logger.info(f'request page - {self.url}')
            
            if r.status_code == 200:
                logger.info(f'request page - status code - 200')
                self.response = BeautifulSoup(r.text, 'html.parser')
            else:
                logger.error(f'error request page - status code - {r.status_code}')
    
        except Exception as e:
            logger.critical(f'error request page - {self.url} - \n {e}')

    def save_data_json(self) -> None:
        """ salvar lote de dados em json
        """
        
        file_path = f'data/{self.batch}/{self.crawler_name}.json'
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.items, json_file, indent=4, ensure_ascii=False)
        logger.info('batch saved in JSON')
    
    def save_data_database(self) -> None:
        """ salvar lote de dados, no banco
        """
        
        for item in self.items:
            item['batch'] = self.batch
            new_item = self.model_item(**item)
            
            try:
                session.add(new_item)
                session.commit()
                logger.info(f'item saved in database - {new_item}')
            except Exception as e:
                session.rollback()
                logger.error(f'error insert, rollback - {e}')
    
    def save(self) -> None:
        """ salvar lote de dados
        """
        
        self.batch_generate()
            
        try:
            self.save_data_json()
        except Exception as e:
            logger.error(f'error saving batch in json - {e}')
        
        try:
            self.save_data_database()
        except Exception as e:
            logger.error(f'error saving batch in database - {e}')
        
        try:
            self.screenshot()
        except Exception as e:
            logger.error(f'error saving screenshot - {e}')

    def batch_generate(self):
        """ gerar lote para salvar os dados
        """
        
        try:
            self.batch = uuid.uuid4()
            os.makedirs(f'data/{str(self.batch)}')
            logger.info(f'batch generated - {str(self.batch)}')
        except Exception as e:
            logger.error(f'error batch generated - {e}')
            
    def screenshot(self):
        """ salvar screenshot da requisição do site
        """
        from utils.screenshot import screenshot
        
        file_path = f'data/{self.batch}/{self.crawler_name}.png'
        screenshot(self.url, file_path)
        logger.info(f'screenshot save - batch {self.batch}')

    @abstractmethod
    def execute(self) -> None: ...