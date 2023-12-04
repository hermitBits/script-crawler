# Script para scraping de páginas

1. [Introdução](#introducao)
2. [Instalação](#instalacao)
3. [Executar](#executar)
4. [Cadastrar um crawler](#cadastro)


<div id="introducao">
<h2>1. Introdução</h2> 

Esse script executa crawlers e seus dados extraidos são persistidos em lotes tanto em arquivos json quanto no banco de dados relacional. Há também screenshot da página no momento da raspagem e salvo juntamento com lote na pasta **data**.

</div>


<div id="instalacao">
<h2>2. Instalação</h2> 

- Build do container Docker:
``` 
docker-compose build
```

- Executar container:
```
docker-compose run script /bin/bash
```

- Rodar migrações:
```
alembic upgrade head
```

</div>

<div id="executar">
<h2>3. Executar</h2>

- Acessar o container Docker:
``` 
docker-compose run script /bin/bash
```

- Executar script:
```
python main.py
```

A interação é interativa, então abrirá menu com a opção de executar de imediato ou fazer um agendamento.

</div>

<div id="cadastro">
<h2>3. Cadastrar um crawler</h2>

Arquivo **scraping/register_crawlers.py**, fica com responsabilidade de cadastrar crawlers que serão executados.
Os Crawlers devem ser extensão de CrawlerBase, nele contém a base para um.

Exemplo de um cadastro de um crawler:
```
from scraping.manager_crawler import ManagerCrawler
from scraping.crawlers.example import CrawlerExample

config = {
    'url': ...,                # url página 
    'crawler_name': ...,       # nome do crawler
    'model_item': ...,         # model do crawler
    ...
    outras parâmetros, exemplo classes css que serão usadas para achar os items na página
}

example = CrawlerExample(config)

manager_commands = ManagerCommands()
manager_commands.add_crawl(example)
```

Exemplo de uma classe de um crawler:
```
from scraping.crawler_base import CrawlerBase

class CrawlerExample(CrawlerBase):
    """ Crawler Example
    """

    def __init__(self, config: Dict):
        super().__init__(
            crawler_name=config.get('crawler_name', 'example_name'),
            url=config.get('url'),
            model_item=config.get('model_item')
        )
        self.config = config

    def execute(self) -> None:
        # request na página
        self.request()
        
        # implementar lógica, o parser da página gerado pelo BeautifulSoup4 está acessivel no atributo self.response.
        print(self.response)

        # salvar dados extraídos
        self.save()
```
</div>