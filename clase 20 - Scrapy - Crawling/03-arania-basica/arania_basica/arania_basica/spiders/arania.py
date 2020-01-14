import scrapy 


class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    

    # def parse(self, response):
    #     etiqueta_contenedora = response.css('article.product_pod')
    #     titulos = etiqueta_contenedora.css('h3 > a::text').extract()
    #     print(titulos)
    

    def parse(self, response):
        #etiqueta_precios = response.xpath("/div[@class = 'product_pod']/p[@class='price']").extract()
        etiqueta_contenedora = response.css('article.product_pod')
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        #precios = etiqueta_contenedora.xpath('div.producto_price > p.price_color').extract()
        for precio in precios:
            
            print(precio[1:])

        # $ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()