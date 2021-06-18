import scrapy

class MusicaCom(scrapy.Spider):
    name = "musica.com"

    def start_requests(self):
        urls = [
            'https://www.musica.com/letras.asp?letras=4324'
        ]
        for url in urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for song in response.css('.listado-letras li'):
            yield {
                'href': song.css('a::attr(href)').get(),
                'text': song.css('.info-letra::text').get()
            }
