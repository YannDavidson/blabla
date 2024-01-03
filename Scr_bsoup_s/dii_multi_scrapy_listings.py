import scrapy

class JobSpider(scrapy.Spider):
    name = "job_spider"

    start_urls = [
        ("Indeed", "https://www.indeed.com/jobs?q={}&l={}", [
            ("title", "h2.jobtitle a::text"),
            ("company", "span.company span::text"),
            # ... other Indeed selectors
        ]),
        ("Monster", "https://www.monster.com/jobs/search/?q={}&where={}", [
            ("title", "div.job-card__title a span::text"),
            ("company", "div.job-card__company-name a::text"),
            # ... other Monster selectors
        ]),
        ("Glassdoor", "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword={}&sc.keyword={}&locT=C&locId={}", [
            ("title", "div.jobsCard_title a::text"),
            ("company", "div.jobsCard_companyLink span::text"),
            # ... other Glassdoor selectors
        ]),
        # ... add other job boards with their respective URLs and selectors
    ]

    # ... (rest of the Spider code to be added)
