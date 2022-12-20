"""
This is the utils of project(where all commonly used functions and constants are stored)
"""
import time
import requests

SYMBOL = "^NSEI" # any symbol from yahoo finance
number_of_candles_to_iterate = 6 # Literally the varable name
TOKEN = '5439333939:AAFSQRPoFSUQCLVrki-9ypYCH5tHyf_KSVE' # Telegram bot token
CHAT_ID = '-1001882134110' # telegram group id

def send_message(message):
    """
    This function sends message to the telegram group.
    """

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)
    time.sleep(2)
