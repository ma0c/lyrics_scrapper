import scrapy

class MusicaCom(scrapy.Spider):
    name = "musica.com"

    def start_requests(self):
        url = 'https://www.musica.com/letras.asp?letras={}'.format(self.artist_id)
        yield scrapy.Request(url, self.parse)

    def parse(self, response, **kwargs):
        yield from response.follow_all(css='.listado-letras li a', callback=self.extract_songs)

    def extract_songs(self, response):
        yield {
            'title': response.css('h1::text').get(),
            'lyrics': '\n'.join(p.get() for p in response.css('#letra p::text'))
        }
