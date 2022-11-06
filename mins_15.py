"""
This is the implementation of the first 15 mins of the market then break out Strategy
"""

import yfinance as yf
import utils as utils


def check_15mins(breaking_candle = 2):
    """
    checks the first 15 mins candle condition
    """
    data =  yf.download(utils.SYMBOL,period ="1d",interval = "15m")
    breaking_candle_for_recursion = 2


    first_candle = data.head(1)
    first_candle_high = first_candle['High']
    first_candle_low = first_candle['Low']

    second_candle = (data.head(breaking_candle)).tail(1)
    second_candle_current = second_candle['Close']

    if int(first_candle_high)<int(second_candle_current):
        print("if.", breaking_candle_for_recursion)
        utils.send_message(f"Bullish. Above {int(first_candle_high)}\nAccording to 15mins candle.")
        return 0
    elif int(first_candle_low)>int(second_candle_current):
        print("elif.", breaking_candle_for_recursion)
        utils.send_message(f"bearish. Above {int(first_candle_low)}\nAccording to 15mins candle.")
        return 0
    else:
        print("else.", breaking_candle_for_recursion)
        breaking_candle_for_recursion += 1
        return check_15mins(breaking_candle=breaking_candle_for_recursion)
