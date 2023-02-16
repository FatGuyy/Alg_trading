import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#---------------------------------------------------------------


SYMBOL = "^NSEI" # any symbol from yahoo finance
data = yf.download(SYMBOL,period ="2d",interval = "5m") # getting data 

#---------------------------------------------------------------


# Simple Moving Average 
def SWMA(data, ndays): 
    SMA = pd.Series(data['Close'].rolling(ndays).mean(), name = 'SMA') 
    data = data.join(SMA) 
    # print(data)
    return data

# Compute the 50-day SMA

n = 50 # n gives time period 
SMA = SWMA(data,n) # calling function

#---------------------------------------------------------------

SMA_data = SMA['SMA'] # getting only SMA data with time

SMA_data_list = SMA_data.values.tolist()

#------------------------------------------------------------------------------------------------

#----------------------------------------------------------------
# Exponentially-weighted Moving Average  
def EWMA(data, ndays): 
    EMA = pd.Series(data['Close'].ewm(span = ndays, min_periods = ndays - 1).mean(), 
                 name = 'EWMA_' + str(ndays)) 
    data = data.join(EMA)
    # print(data)
    return data

# Compute the 5-day EWMA

ew = 5
EWMA = EWMA(data,ew)

#---------------------------------------------------------------

EWMA_data = EWMA['EWMA_5'] # getting only SMA data with time

EWMA_data_list = EWMA_data.values.tolist() # converting data into list

for i in range(0,len(SMA_data_list)-1):

    if EWMA_data_list[i] == 'NaN' and SMA_data_list[i] == 'NaN': continue
    else :
        # EWMA_data_list[i] = int(EWMA_data_list[i])
        # SMA_data_list[i] = int(SMA_data_list[i])

    #For Bullish

        if SMA_data_list[i] > EWMA_data_list[i] and EWMA_data_list[i+1] > SMA_data_list[i+1] : 
            print("Getting Bulish")
            print("From : " , SMA_data_list[i+1])
        # else : print("No Bulish ")

    #For Bearish

        if(EWMA_data_list[i] > SMA_data_list[i] and SMA_data_list[i+1] > EWMA_data_list[i+1]) : 
            print("Getting Bearish")
            print("From : " , EWMA_data_list[i+1])
        # else : print("No Bearish ")

