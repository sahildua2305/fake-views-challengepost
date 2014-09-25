import requests
import time
import random

code=200
i=1
while code==200:
    r = requests.get('http://challengepost.com/software/github-profile-scraper')
    code = r.status_code
    delay = random.randint(1,5)
    print i,delay,r
    i+=1
    time.sleep(delay)
