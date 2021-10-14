from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

def findPledged(page):
    the_page = page.readlines()   # read html file  
    for line in the_page:             # go through the lines             
        lineStr = str(line, encoding='utf8')  # put the lines in readable form (utf8)
        if '<span data-test-id="amount-pledged">' in lineStr: # search for this string
            words = lineStr.split(',') # split the line into words 
            for word in words:    # loop over each word
                 if '<span data-test-id="amount-pledged">' in word:  # look for datetime=
                    target = (word.split('</span>',1)) # split the word at <
                    date_target = target[0] 
                    dateStr = float(date_target.strip('<span data-test-id="amount-pledged">'))  
                    return dateStr

def scraper(url):
    browser = webdriver.Chrome()
    browser.get(url)
    page = browser.page_source
    return page

def interface():
    print("Art - 1\nTechnology - 16\n ")
    option = input("Please select a category:")
    url = "https://www.kickstarter.com/discover/advanced?category_id=" + option + "&sort=newest&seed=2723668&page=1"
    print(url)
    findPledged(scraper(url))
interface()