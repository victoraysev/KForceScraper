import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from fit_checker import evaluate_job_fit
from get_job_detail import get_job_detail
from to_word import to_word

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox() if you're using Firefox
driver.get('https://www.kforce.com/find-work/search-jobs/#/?t=Java&l=%5B%5D')

# Click "Load more" until it no longer appears
while True:
    try:
        driver.find_element("xpath", "//span[@class='btn-line-darkCerulean' and text()='Load more']").click()
        time.sleep(2)  # Wait for the next set of jobs to load
    except:
        break  # Exit the loop when the "Load more" button is no longer found

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the Selenium WebDriver
driver.quit()

# Find all job links
job_links = soup.find_all('a', class_='linkForJob')

# List to store job data
jobs = []

# Iterate over each job link
for job_link in job_links:
    # Extract the href attribute
    job_href = job_link['href']
    # Construct the full URL
    job_url = 'https://www.kforce.com/find-work/search-jobs/' + job_href

    try:
        job_data = get_job_detail(job_url)
    except:
        print("Error")
        print(job_url)
        continue
    job_description = job_data['Description']
    job_title = job_data['Title']

    fit_checker = evaluate_job_fit(job_description)

    if fit_checker:
        jobs.append({ 'Link': job_url, 'Description': job_description, 'Title': job_title })


to_word(jobs)

print("Job titles, links, and descriptions have been exported to kforce_jobs_details.xlsx")
