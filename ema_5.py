"""
This is the 5 ema strategy implimentation.
"""
import yfinance as yf
import utils

def ema_5():
    data =  yf.download(utils.SYMBOL,period ="1d",interval = "5m")
    data_10 = data.tail(utils.number_of_candles_to_iterate)
    data_10.reindex()

    index_time = data_10.index
    index_time_tolist_2 = []
    index_time_tolist = index_time.tolist() #converting to list

    for timestamp in index_time_tolist:
        time = (str(timestamp))
        index_time_tolist_2.append(time)
    
    # getting lower values of recent data
    data_high = data[["High"]].tail(utils.number_of_candles_to_iterate)
    data_high_values_tolist = data_high.values.tolist() # converting data into list

    # getting lower values of recent data
    data_low = data[["Low"]].tail(utils.number_of_candles_to_iterate)
    data_low_values_tolist = data_low.values.tolist() # converting data into list

    # exponential moving average
    data['ema'] = data['Close'].ewm(span=5).mean()
    data_ema = data['ema'].tail(utils.number_of_candles_to_iterate)
    data_ema_values_tolist = data_ema.values.tolist() # converting data into list

    def bullish_market():
        """
        This function takes input and gives signal if data is bullish
        """
        if(ema_candle_1st_value <= high_candle_1st_value and ema_candle_2nd_value >= high_candle_2nd_value and ema_candle_3rd_value <= high_candle_3rd_value and high_candle_3rd_value > high_candle_1st_value and low_candle_2nd_value < low_candle_3rd_value):
            high_candle_3rd_str = str(high_candle_3rd_value)
            var =f'Bullish Market.\nBuy CE above level : {high_candle_3rd_str}\n' + f'SL is {low_candle_2nd_value}'
            return(var + f'\nTime = {index_time_3rd_candle}')
        return "None"

    def bearish_market():
        """
        This function takes input and gives signal if data is bearish.
        """
        if(ema_candle_1st_value >= low_candle_1st_value and ema_candle_2nd_value <= low_candle_2nd_value and ema_candle_3rd_value >= low_candle_3rd_value and low_candle_3rd_value < low_candle_1st_value and high_candle_2nd_value > high_candle_3rd_value ):
            low_candle_3rd_str = str(low_candle_3rd_value)
            var = f'Bearish Market.\nBuy PE bellow level :  {low_candle_3rd_str} \n' + f'SL is {high_candle_2nd_value}'
            return(var + f'\nTime = {index_time_3rd_candle}')
        return "None"

    for i in range(0,len(data_high_values_tolist)-2):

            # Get index i.e time
            index_time_1st_candle = index_time_tolist_2[i]
            index_time_2nd_candle = index_time_tolist_2[i+1]
            index_time_3rd_candle = index_time_tolist_2[i+2]

            # storing recent 3 candle's higher values
            high_candle_1st_value = data_high_values_tolist[i][0]
            high_candle_2nd_value = data_high_values_tolist[i+1][0]
            high_candle_3rd_value = data_high_values_tolist[i+2][0]

            # storing recent 3 candle's lower values
            low_candle_1st_value = data_low_values_tolist[i][0]
            low_candle_2nd_value = data_low_values_tolist[i+1][0]
            low_candle_3rd_value = data_low_values_tolist[i+2][0]

            # getting ema values
            ema_candle_1st_value = data_ema_values_tolist[i]
            ema_candle_2nd_value = data_ema_values_tolist[i+1]
            ema_candle_3rd_value = data_ema_values_tolist[i+2]

            bullish_message = bullish_market()
            bearish_message = bearish_market()
            if 'Bullish Market.' in bullish_message:
                utils.send_message(bullish_message)
                # print(bullish_message)

            elif 'Bearish Market.' in bearish_message:
                utils.send_message(bearish_message)
                # print(bearish_message)