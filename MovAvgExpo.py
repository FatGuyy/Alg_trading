import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

SYMBOL = "^NSEI" # any symbol from yahoo finance
data = yf.download(SYMBOL,period ="10d",interval = "15m")

# Exponentially-weighted Moving Average  
def EWMA(data, ndays): 
    EMA = pd.Series(data['Close'].ewm(span = ndays, min_periods = ndays - 1).mean(), 
                 name = 'EWMA_' + str(ndays)) 
    data = data.join(EMA)
    print(data)
    return data

# Compute the 5-day EWMA

ew = 5
EWMA = EWMA(data,ew)