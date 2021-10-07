
from urllib.request import Request, urlopen, URLError

def checkResponse(response):
    the_page = response.readlines()   # read html file  
    for line in the_page:             # go through the lines             
        lineStr = str(line, encoding='utf8')  # put the lines in readable form (utf8)
        if 'var properties = JSON.parse(`{"session_client":' in lineStr: # search for this string
            words = lineStr.split(',') # split the line into words 
            for word in words:    # loop over each word
                 if '"project_current_amount_pledged_usd":' in word:  # look for datetime=
                    target = (word.split(',"project_deadline":',1)) # split the word at <
                    date_target = target[0] 
                    dateStr = float(date_target.strip('project_current_amount_pledged_usd":'))  
                    return dateStr
               
                            
def checkKickstarter(url):  # this function starts the url request
    req = Request(url)
    try:
        response = urlopen(req)
    except URLError:
        print("There was an error.")
    else:
        print(checkResponse(response))


# this is the website and initial function call
someurl='https://www.kickstarter.com/projects/oinkgames/new-oink-games-projects-2021?ref=section-games-view-more-discovery-p1'
checkKickstarter(someurl)    # this starts the program

