import requests
import os
import random
import json
import time
import schedule
random.seed = (os.urandom(1024))

url = '***URL_REMOVED***'
first_name = "Evan"
last_name = "Hughes"
excuses = json.loads(open('excuse.json').read())
excuse = random.choice(excuses)

def check_in():
    requests.post(url, allow_redirects=False, data={
        '***DATA***' :  last_name,
        '***DATA***' : first_name,
        '***DATA***' : excuse
    })
