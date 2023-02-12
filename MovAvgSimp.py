import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

SYMBOL = "^NSEI" # any symbol from yahoo finance
data = yf.download(SYMBOL,period ="10d",interval = "15m")
# Simple Moving Average 
def SMA(data, ndays): 
    SMA = pd.Series(data['Close'].rolling(ndays).mean(), name = 'SMA') 
    data = data.join(SMA) 
    print(data)
    return data

# Compute the 50-day SMA

n = 50
SMA = SMA(data,n)