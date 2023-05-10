import yfinance as yf

equity = yf.Ticker("^NSEI")
data = equity.history(period='1d', interval='15m')
df = data[['Close']]

sma = df.rolling(window=20).mean().dropna()
rstd = df.rolling(window=20).std().dropna()

upper_band = sma + 1.5 * rstd
lower_band = sma - 1.5 * rstd

upper_band = upper_band.rename(columns={'Close': 'upper'})
lower_band = lower_band.rename(columns={'Close': 'lower'})
bb = df.join(upper_band).join(lower_band)

#-------------------------------------------------------------------------

bb_upper = bb['upper'] #getting upper band values only
bb_lower = bb['lower'] # getting lower band values only

# print(bb_upper)
# print(bb_lower)

#-------------------------------------------------------------------------------
# converting into list

bb_upper_list = bb_upper.values.tolist()
bb_lower_list = bb_lower.values.tolist()
print(bb_upper_list)
print(bb_lower_list)

#----------------------------------------------------------------------------------
