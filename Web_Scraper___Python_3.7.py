from selenium import webdriver
def scraper(url):
    browser = webdriver.Chrome()
    browser.get(url)
    page = browser.find_elements_by_xpath('/html/body/main/div/section/section[2]/div[3]/div/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/div[1]/span[1]')
    print(page)

def interface():
    print("Art - 1\nTechnology - 16\n ")
    option = input("Please select a category:")
    url = "https://www.kickstarter.com/discover/advanced?category_id=" + option + "&sort=newest&seed=2723668&page=1"
    print(url)
    scraper(url)
interface()