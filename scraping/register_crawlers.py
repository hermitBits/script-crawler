from scraping.crawlers.quotes import Quotes
from scraping.manager_crawler import ManagerCrawler

config = {
    'url': 'https://quotes.toscrape.com/',
    'class_quote': '.quote',
    'class_author': '.author',
    'class_text': '.text',
    'class_keywords': '.keywords'
}

quotes = Quotes(config)

manager = ManagerCrawler()
manager.add_crawler(quotes)
