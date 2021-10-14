from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

def findPledged(page):


def scraper(url):
    browser = webdriver.Chrome()
    browser.get(url)
    page = browser.page_source
    print(page)

def interface():
    print("Art - 1\nTechnology - 16\n ")
    option = input("Please select a category:")
    url = "https://www.kickstarter.com/discover/advanced?category_id=" + option + "&sort=newest&seed=2723668&page=1"
    print(url)
    scraper(url)
interface()