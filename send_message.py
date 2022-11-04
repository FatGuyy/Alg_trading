"""
This is the telegram side of the project.
"""
import time
import requests
import telepot


TOKEN = '5439333939:AAFSQRPoFSUQCLVrki-9ypYCH5tHyf_KSVE'
CHAT_ID = '-1001882134110'
bot = telepot.Bot(TOKEN)

def send_message(message):
    """
    This function sends message to the telegram group.
    """

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)
    # print(requests.get(url).json())
    time.sleep(2)
