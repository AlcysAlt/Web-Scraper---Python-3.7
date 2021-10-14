from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time

def getPledged(page):
    soup = BeautifulSoup(page, 'html.parser')
    
    for span in soup.findAll("span", {"data-test-id": "amount-pledged"}):
        print(span.text)
    
def scraper(url):
    browser = webdriver.Chrome()
    browser.get(url)
    page = browser.page_source
    return page

def interface():
    print("Art - 1\nTechnology - 16\n ")
    option = input("Please select a category: ")
    url = str("https://www.kickstarter.com/discover/advanced?category_id=" + option + "&sort=newest&seed=2723668&page=")
    maxPages = int(input("Please enter the amount of pages to scrape: "))

    for i in range(1, maxPages + 1):
        tempUrl = url + str(i)
        print(tempUrl)
        getPledged(scraper(tempUrl))
        print("Next Page")
        time.sleep(1)
    


interface()

