'''
#------------------------------------------------------
# BOLINGER-BANDS

# give prices as list  # rate = 20 
def get_sma(prices, rate):
    return prices.rolling(rate).mean()

def get_bollinger_bands(prices, rate=20, std_dev = 2):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * std_dev # Calculate top band
    bollinger_down = sma - std * std_dev # Calculate bottom band
    return bollinger_up, bollinger_down
#------------------------------------------------------
'''

# Middle band is 20 day sma.
# Upper = 20sma + some std deviation.
# give prices as list  # rate = 20 
def get_sma(prices, rate):
    return prices.rolling(rate).mean()

def get_bollinger_bands(prices, rate=20, std_dev = 2):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * std_dev # Calculate top band
    bollinger_down = sma - std * std_dev # Calculate bottom band
    return bollinger_up, bollinger_down

# symbol = '^NSEI'
# df = pdr.DataReader(symbol, 'yahoo', '2014-07-01', '2015-07-01')
# df.index = np.arange(df.shape[0])
# closing_prices = df['Close']

# bollinger_up, bollinger_down = get_bollinger_bands(closing_prices) 