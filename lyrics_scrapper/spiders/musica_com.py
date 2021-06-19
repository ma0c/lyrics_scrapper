import scrapy

class MusicaCom(scrapy.Spider):
    name = "musica.com"

    start_urls = ['https://www.musica.com/letras.asp?letras=4324']

    def parse(self, response, **kwargs):
        yield from response.follow_all(css='.listado-letras li a', callback=self.extract_songs)

    def extract_songs(self, response):
        yield {
            'title': response.css('h1::text').get(),
            'lyrics': '\n'.join(p.get() for p in response.css('#letra p::text'))
        }
