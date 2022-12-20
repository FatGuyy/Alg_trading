"""
This file just sums up all the files and runs them.
"""
from time import sleep
import schedule
import hackathon.SITS.utils as utils
from ema_5 import ema_5 as ema_5

schedule.every().day.at("3:45").do((ema_5.ema_5()))

# run_once = True
while True:

    schedule.run_pending()
    sleep(300)
