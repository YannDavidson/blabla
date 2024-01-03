import requests
from bs4 import BeautifulSoup

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Refer to Selectors Folder to add more selectors for specific job boards
    job_elements = soup.find_all("div", class_="job_listing")  # Example selector

    jobs = []
    for job_element in job_elements:
        title = job_element.find("h2").text
        company = job_element.find("span", class_="company").text
        location = job_element.find("span", class_="location").text

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            # Extract additional fields as needed
        })

    return jobs

# Example usage
indeed_jobs = scrape_jobs("https://www.indeed.com/jobs?q=software+engineer&l=Austin%2C+TX")
Simplyhired = scrape_jobs("https://www.simplyhired.com/search?q=python&l=Austin%2C+TX")

