import scrapy
import re

# change accordingly
username = "dericored"
period = ["2020/01/01", "2022/01/01"] # [from, to] in YYYY/MM/DD

class LetterboxdSpider(scrapy.Spider):
    name = "diary"
    start_urls = [
        f'https://letterboxd.com/{username}/films/diary/'
    ]

    def parse(self, response):
        for post in response.css('.diary-entry-row'):
            rel_url = "https://letterboxd.com" +  post.css('.td-film-details h3 a::attr("href")')[0].get().replace(f"/{username}", "")
            title = post.css('.td-film-details h3 a::text')[0].get()
            watch_date = post.css('.td-day a::attr("href")')[0].get()[-11:-1]
            released_year = post.css('.td-released span::text')[0].get()
            my_rating = int(post.css('.td-rating input::attr("value")')[0].get())/2
            like = bool(len(post.css(".td-like .has-icon[class*='icon-liked']")))
            rewatch =  not(bool(len(post.css(".td-rewatch[class*='icon-status-off']"))))

            if watch_date < period[0]: break;
            if watch_date > period[1]: continue;

            details = {
                'title': title,
                'link': rel_url,
                'watch_date': watch_date,
                'released_year': released_year,
                'my_rating': my_rating,
                'like': like,
                'rewatch': rewatch
            }

            yield scrapy.Request(rel_url, callback=self.parse_details, meta=details)

        next_page = response.css('.paginate-nextprev .next::attr("href")').get()
        if next_page is not None:
            # or: yield response.follow(next_page, callback=self.parse)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_details(self, response) :
        director = response.css('#featured-film-header p a span::text').getall()
        tagline = response.css('.review .tagline::text').get()
        synopsis = response.css('.truncate p::text')[0].get()
        # remove uncredited actors
        actor = response.css('#tab-cast .cast-list p a:not([title*="uncredited"])::text').getall()
        # remove "Show All..."
        actor = [x for x in actor if not x.startswith("Show")]
        producer = response.css('#tab-crew div:nth-child(4) p a::text').getall()
        writer = response.css('#tab-crew div:nth-child(6) p a::text').getall()
        editor = response.css('#tab-crew div:nth-child(8) p a::text').getall()
        cinematographer = response.css('#tab-crew div:nth-child(10) p a::text').getall()
        composer = response.css('#tab-crew div:nth-child(20) p a::text').getall()
        studio = response.css('#tab-details div:nth-child(2) p a::text').getall()
        country = response.css('#tab-details div:nth-child(4) p a::text').getall()
        language = response.css('#tab-details div:nth-child(6) p a::text').getall()
        genre = response.css('#tab-genres div:nth-child(2) p a::text').getall()
        rating = float(response.css('meta[name="twitter:data2"]::attr(content)').get().split(" ")[0])
        runtime = response.css(".section.col-10.col-main .text-link.text-footer::text").get()
        # extract runtime from gibberish string
        runtime = int(re.findall('[0-9]+',runtime)[0])

        yield {
            'title': response.meta['title'],
            'director': director,
            'tagline': tagline,
            'synopsis': synopsis,
            'link': response.meta['link'],
            'released_year': response.meta['released_year'],
            'actor': actor,
            'producer': producer,
            'writer': writer,
            'editor': editor,
            'cinematographer': cinematographer,
            'composer': composer,
            'studio': studio,
            'country': country,
            'language': language,
            'genre': genre,
            'rating': rating,
            'runtime': runtime,
            'watch_date': response.meta['watch_date'],
            'my_rating': response.meta['my_rating'],
            'like': response.meta['like'],
            'rewatch': response.meta['rewatch']
        }

# Run script: scrapy crawl diary -O scraped.json
