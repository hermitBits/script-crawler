import json
import requests
import os
import uuid


from datetime import datetime
from abc import abstractmethod
from bs4 import BeautifulSoup

from scraping import logger


class Crawler():
    """ Classe para base de um crawler
    """
    
    def __init__(self, crawler_name, url):
        self.url = url
        self.crawler_name = crawler_name
        self.items = []
        # self.model_item = model_item
        self.current_date = None
        self.batch = None
        self.response = None
        
    def request(self) -> None:
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
        file_path = f'data/{self.batch}/{self.crawler_name}_data-{self.current_date}.json'
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.items, json_file, indent=4, ensure_ascii=False)
        logger.info('batch saved in JSON')
    
    def save(self) -> None:
        self.current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        
        # gerar lote de dados
        self.batch_generate()
            
        try:
            self.save_data_json()
        except Exception as e:
            logger.error(f'error saving batch - {e}')

    def batch_generate(self):
        try:
            self.batch = str(uuid.uuid4())
            os.makedirs(f'data/{self.batch}')
            logger.info(f'batch generated - {self.batch}')
        except Exception as e:
            logger.error(f'error batch generated - {e}')

    @abstractmethod
    def execute(self) -> None: ...