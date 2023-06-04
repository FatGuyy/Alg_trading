"""
This is the utils of project(where all commonly used functions and constants are stored)
"""
import time
import requests

TOKEN = '' # Enter your telegram bot token
CHAT_ID = '' # Enter your telegram group id

def send_message(message):
    """
    This function sends message to the telegram group.
    """

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)
    time.sleep(2)
