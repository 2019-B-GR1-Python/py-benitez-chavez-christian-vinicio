import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AraniaCrawlOnu(CrawlSpider):
    name = "crawl_onu"

    allowed_domains = [
        'un.org'
    ]

    start_urls = {
        'https://www.un.org/es/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    }

    regla_uno = (
        Rule(LinkExtractor(), callback='parse_page')
        ,
    )

    url_segmento_permitido = (
        'funds-programmes-specialized-agencies-and-others'
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = url_segmento_permitido
            ), callback ='parse_page'
        ),
    )

    url_segmento_restringido = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )

    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = url_segmento_permitido,
                deny = url_segmento_restringido
            ), callback = 'parse_page'
        ),
    )


    rules = regla_dos

    def parse_page(self, response):
        lista_programas_onu = response.css('div.field-items > div.field-item > h4::text').extract()
        for agencia in lista_programas_onu:
            with open('onu_agencias.txt','a+', encoding = 'utf-8') as archivo:
                archivo.write(agencia+'\n')