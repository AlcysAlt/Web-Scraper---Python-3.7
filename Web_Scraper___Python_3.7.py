import time
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from price_parser import Price
from currency_converter import CurrencyConverter

currencyDict={"$":"USD","HK$":"HKD","€":"EUR","£":"GBP","S$":"SGD","CA$":"CAD","CHF":"CHF","MX$":"MXN","AU$":"AUD","¥":"JPY","DKK":"DKK"}
c = CurrencyConverter()
def currencyParsing(currencySymbol, amount):
    return round(c.convert(amount, currencyDict.get(currencySymbol), 'USD'), 2)
    


def getPledged(page):
    soup = BeautifulSoup(page, 'html.parser')
    pledged = 0.0
    for span in soup.findAll("span", {"data-test-id": "amount-pledged"}):
        pledge = Price.fromstring(span.text)
        pledged = pledged + currencyParsing(pledge.currency, pledge.amount_float)
    return pledged


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
    print("Total amount pledged: $", totalPledged)


interface()

