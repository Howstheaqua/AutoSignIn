import time
import schedule

def joob():
    print("worked")


schedule.every().monday.at("11:51").do(joob)
while True:
    schedule.run_pending()
    time.sleep(1)
