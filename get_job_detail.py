from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# URL of the job detail page
job_url = 'https://www.kforce.com/find-work/search-jobs/#/detail/MTY5Nn5FUUd-MjExNzgzN1Qxfjk5/'

def get_job_detail(job_url):
    # Set up Selenium WebDriver (Make sure you have the correct ChromeDriver version)
    driver = webdriver.Chrome()  # or webdriver.Firefox() if you're using Firefox
    driver.get(job_url)

    # Get the page source after the page has fully loaded
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Close the Selenium WebDriver
    driver.quit()

    # Extract the job title
    job_title = soup.find('h1', class_='col-xs-12 col-sm-8').text.strip()

    # Extract the job description
    job_description = soup.find('div', class_='col-xs-12 col-sm-12 data-job-desc').find('p').text.strip()

    # Store the data in a dictionary
    job_data = {
        'Title': job_title,
        'Link': job_url,
        'Description': job_description
    }

    # Create a DataFrame with a single row
    return job_data
# x = get_job_detail(job_url)
# print(x)