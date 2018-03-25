import scrapy

class LeadersSpider(scrapy.Spider):
    name = "leaders"

    start_urls = [
        "http://www.quanthockey.com/nhl/seasons/2017-18-nhl-players-stats.html"
    ]

    def parse(self, response):
        for player in response.css('tr')[2:]:
            td = player.css('td::text').extract()
            yield {
                'rank': td[0],
                'name': player.css('a::text').extract_first(),
                'position': td[2],
                'gp': td[3],
                'goals': td[4],
                'assists': td[5],
                'points': td[6],
                'pim': td[7],
                'PlusMinus': td[8]
            }
