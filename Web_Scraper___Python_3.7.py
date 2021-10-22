import os
import time
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from price_parser import Price
from currency_converter import CurrencyConverter

#Converts currency symbols used by kickstarter into symbols that can be used with the Currency Converter
currencyDict={"$":"USD",
              "HK$":"HKD",
              "€":"EUR",
              "£":"GBP",
              "S$":"SGD",
              "CA$":"CAD",
              "CHF":"CHF",
              "MX$":"MXN",
              "AU$":"AUD",
              "¥":"JPY",
              "DKK":"DKK",
              "None":"USD",
              "none":"USD"}

optionsDict={"art":1,
             "comics":3,
             "crafts":26,
             "dance":6,
             "design":7,
             "fashion":9,
             "film&video":11,
             "food":10,
             "games":12,
             "journalism":13,
             "music":14,
             "photography":15,
             "publishing":18,
             "technology":16,
             "theater":17}
c = CurrencyConverter()
#Converts currency into USD so it can be added up into a total
def currencyParsing(money):
    try:
        convertedMoney = float(c.convert(money.amount_float, currencyDict.get(money.currency), 'USD')) 
        return convertedMoney 
    except:
        return 0.0
          
    
#Finds and extracts the pledge amounts from the page
def getPledged(page):
    soup = BeautifulSoup(page, 'html.parser')
    pledged = 0.0
    for span in soup.findAll("span", {"data-test-id": "amount-pledged"}):
        pledged = pledged + currencyParsing(Price.fromstring(span.text))
    return pledged

#Finds and extracts amount of search results
def getResultsFound(page):
    soup = BeautifulSoup(page, 'html.parser')
    pledged = 0.0
    for bclass in soup.findAll("b", {"class": "count ksr-green-500"}):
        totalResults = Price.fromstring(bclass.text)
    return totalResults.amount_float

#Scraper which can be used to download the website, can be swapped out for a different one as long as it returns html for use with BeautifulSoup
def scraper1(url):
    browser = webdriver.Chrome()
    browser.get(url)

    page = browser.page_source
    return page

#Interface for taking input for scraping the total pledged
def scrapeTotalPledged():
    print("Here are the categories: \n")
    for category, value in optionsDict.items():
        print(category,"\n-------------")

    option = input("Please select a category: ")

    #The category is set by the user and is used to modify the url to navigate  the website
    url = str("https://www.kickstarter.com/discover/advanced?category_id=" + option + "&sort=newest&seed=2723668&page=")
    maxPages = int(input("Please enter the amount of pages to scrape: "))
    totalPledged = 0.0
    for i in range(1, maxPages + 1):
        tempUrl = url + str(i)
        print(tempUrl)
        totalPledged = totalPledged + getPledged(scraper1(tempUrl))
        time.sleep(1) #Pauses for 1 second before running the scraper again, prevents triggering ddos protection
    print("Total amount pledged: $", round(totalPledged,2))
    
#Interface for taking input for scraping the amount of search results
def scrapeSearchResults():
    searchTerms = []
    resultsFreq = {}
    search = ''
    loop = 1
    print("Please enter the search terms one at a time, if you want to start the scraper, write 'start'")
    while loop == 1:
        search = input("Please enter a search term:\n") 
        if 'start' in search:
            loop = 0
            break
        else:
            searchTerms.append(search)
        

    for term in searchTerms:
        url = "https://www.kickstarter.com/discover/advanced?ref=nav_search&term=" + term
        resultsFreq[term] = float(getResultsFound(scraper1(url)))

    for searchTerm in resultsFreq.items():
        print(searchTerm, '\n')
        
    print("The search result with the most amount of results is: ", max(resultsFreq,key= lambda x: resultsFreq[x]))



#This starts the web scraper
scrapeSearchResults()
os.system("pause")

