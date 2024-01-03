import scrapy

class JobSpider(scrapy.Spider):
    name = "job_spider"
    allowed_domains = ['examplejobboard.com']
    start_urls = ["https://www.indeed.com/jobs?q={}&l={}", "https://www.linkedin.com/jobs/search/?keywords={}"] 

    def parse(self, response):
    
        job_titles = response.css("h2.jobTitle::text").getall()
        companies = response.css("span.companyName::text").getall()
        locations = response.css("span.companyLocation::text").getall()

        for title, company, location in zip(job_titles, companies, locations):
            yield {
                "title": title,
                "company": company,
                "location": location,
                
            }

        # suggestion pagination links for navigating multiple pages
        next_page = response.css("a.pagination-next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
