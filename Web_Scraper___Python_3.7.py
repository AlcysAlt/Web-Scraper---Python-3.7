from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
from price_parser import Price
import requests


def getPledged(page):
    soup = BeautifulSoup(page, 'html.parser')
    totalPledged = 0.0
    for span in soup.findAll("span", {"data-test-id": "amount-pledged"}):
        pledge = Price.fromstring(span.text)
        print(pledge.currency)
        totalPledged = totalPledged + pledge.amount_float
    return totalPledged


def scraper1(url):
    browser = webdriver.Chrome()
    browser.get(url)

    page = browser.page_source
    return page


def interface():
    print("Art - 1\nTechnology - 16\n ")
    option = input("Please select a category: ")
    url = str("https://www.kickstarter.com/discover/advanced?category_id=" + option + "&sort=newest&seed=2723668&page=")
    maxPages = int(input("Please enter the amount of pages to scrape: "))
    totalPledged = 0.0
    for i in range(1, maxPages + 1):
        tempUrl = url + str(i)
        print(tempUrl)
        totalPledged = totalPledged + getPledged(scraper1(tempUrl))
        print("Next Page")
        time.sleep(1)
    print("Total amount pledged:", totalPledged)


interface()

