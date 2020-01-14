# Scrapy
## Scrapy instalación

Ejecutar dentro del `Anaconda prompt`.

```
$ conda install -c conda-forge scrapy
```

## Comandos generales
Da las caracteristicas para poder hacer `Web scraping` o `Web crawling` de ese computador.
```
$ scrapy bench
```
Visualizar las `configuraciones extras`.
```
$ scrapy settings
```
Visualizar la `versión` de Scrapy.
```
$ scrapy version
```

### scrapy view `url`.

Redirecciona a la página web mostrándo el contenido de la misma, en caso de no verse el contenido es debido
a que existe servidores que redireccionan.
```
$ scrapy view https://www.pluralsight.com/authors#
```

## scrapy shell `url`.
Interactuar con la respuesta del scrapy

```
$ scrapy shell http://quotes.toscrape.com/tag/love/
```

```
$ response.css('title')
$ response.css('title').extract
$ response.css('title::text').extract
$ response.css('.author').extract
$ response.css('.author::text').extract
$ type(response.css('.author').extract)
$ response.css('.author::text')[0]
$ response.css('.author::text')[0].extract
$ response.css('.author::text')[0].extract_first()
$ response.css('span.text::text')extract()
$ response.css('div.tags > a.tag::text').extract()
$ response.css('div.tags > a.tag::attr(href)').extract()
$ response.css('div.quote > span > a::attr(href)').extract()
$ response.css('.row > div > div::nth(2) > .text').extract()
$ response.xpath('html/head/title').extract()
$ response.xpath('//title').extract()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ response.xpath("//div[@class='quote']/span/a/@href").extract_first()
$ response.xpath("//div[@class='quote']/span/a/text()").extract_first()
```

## Scrapy startproject `nombre_proyecto`

```
$ scrapy startproject arania_basica
```