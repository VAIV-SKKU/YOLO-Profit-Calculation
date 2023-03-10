import pandas as pd
import exchange_calendars as xcals
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick2_ochl, volume_overlay
from matplotlib import pyplot as plt, dates as mdates
from datetime import datetime as dt
import exchange_calendars as xcals 
import os
import pandas as pd
import os
import glob
import csv

# This file creates an individual csv file for each stock which displays the profit that happens after each transaction.
# To calculate the average profit / transaction profit, use the python files inside the 'cal' folder of this directory.

buy_date = None
ticker= None
sell_date = None
profit_sign = None  
profit_co=0
profit_only=0
counter = 0
buy_check = 0

profit_dict=[]

plus_count=0
profit_plus_aggre_co=0
profit_plus_aggre=0
minus_count=0
profit_minus_aggre_co=0
profit_minus_aggre=0
csv_files = []
count  = 0
row = 0
BUY = "BUY"
SELL = "SELL"

# creating empty lists
date = []
label = []
ticker = []
close =[]
probability = []
i = 0

print("Outside")
path = os.path.join("[DETECT_CSV_FILE_PATH]")

csv_files = glob.glob(path + "/*.csv")


for file in csv_files:

    filename = open(file, "r")

    csv_file = csv.DictReader(filename)
    date = []
    label = []
    ticker = []
    close =[]
    probability = []
    seed = 10000000
    buy_check = 0
        
        # iterating over each row and append
        # values to empty list
    for col in csv_file:
        ticker.append(col['Ticker'])
        date.append(col['Date'])
        label.append(col['Label'])
        close.append(col['Close'])
        probability.append(col['Probability'])

    print(ticker[0]) # prints out the stock that is currently being calculated
    XKRX = xcals.get_calendar("XKRX")
    pred_Dates = XKRX.sessions_in_range("2019-01-01","2021-12-31")
    pred_Dates = pred_Dates.strftime("%Y-%m-%d").tolist()

    for i in range(len(label)):

        if label[i] == "buy" and "2021" in date[i]: #: # If it is a 'BUY' (BUY == 1) and the transaction date is in 2021
            if buy_check == 0:

                buy_check = 1
                ticker_check = ticker[i]  # Records the ticker of the 'BUY' signal (?????????)

                                            # buy_index = trading_index # The 'BUY' index is simply -1 index of the 'BUY" signal
                                            # We set the buy_index -1 of the 'SELL' index.
                buy_date = date[i] # We gather info on the dates as well

                buy_price = close[i]  # We gather information on the price index as well

                                            #We use this to calculate the profit of the BUY and SELL signals

                buy_probability = probability[i] #We gather information on the probability as well
                buy_date_str = str(buy_date)
                buy_date_datetime = dt.strptime(buy_date_str, '%Y-%m-%d')


        if label[i] == "sell" and "2021" in date[i]:
            if buy_check == 1:
                buy_check = 0 
                ticker_check = ticker[i]  # Records the ticker of the 'BUY' signal (?????????)

                sell_index = 1 # The 'BUY' index is simply -1 index of the 'BUY" signal
                            # We set the buy_index -1 of the 'SELL' index.
                sell_date = date[i] # We gather info on the dates as well
                                    #  sell_date = old_df['Date'][trading_index] 
                sell_price = close[i]  # We gather information on the price index as well
                                        #  sell_price = old_df['Close'][trading_index]
                                        #We use this to calculate the profit of the BUY and SELL signals

                sell_probability = probability[i] #We gather information on the probability as well
                buy_date_str = str(sell_date)
                buy_date_datetime = dt.strptime(buy_date_str, '%Y-%m-%d')
                profit_only =  round( ( (float(sell_price) *0.9975) - float(buy_price) ) / float(buy_price) * 100, 3 )
                seed = round((seed * profit_only / 100)  + seed,2)
                total_profit = round(((seed - 10000000) / 10000000 )* 100,2 )

                                        #+ ?????????
                if profit_only > 0 and sell_index == 1:
                    plus_count+=1
                    profit_sign = '+'
                    profit_plus_aggre+=profit_only
                    profit_plus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability,  sell_date, sell_price, sell_probability, profit_only, seed, profit_sign, total_profit ]
                    profit_dict.append(profit_row)

                                        
                                        #- ?????????
                elif profit_only < 0 and sell_index == 1:
                    minus_count+=1
                    profit_sign = '-'
                    profit_minus_aggre+=profit_only
                    profit_minus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability,  sell_date, sell_price, sell_probability, profit_only, seed, profit_sign ,total_profit]
                    profit_dict.append(profit_row)


                                        

                                                        
                    #2 buy-sell pair dataframe ??????
                

    profit_pair_df = pd.DataFrame(profit_dict,columns=['Ticker','Buy_Date','Buy_Price','Buy_Prob', 'Sell_Date','Sell_Price', 'Sell_Prob', 'Pair_Profit', 'Principal', 'Profit' ,'Total Profit'])
                    #3 dataframe??? csv??? ??????

    profit_pair_df.sort_values(by='Buy_Date', inplace= True) # ????????? ?????? ?????? ??????, ????????????.
    profit_pair_df.reset_index(inplace=True, drop=True)
    title = f"{ticker_check}_2021_profit.csv" # csv ?????? ?????? ??????
    profit_pair_df.to_csv(title,encoding='UTF-8-sig',index='False')
    profit_dict.clear()
    seed = 10000000 # resets the seed to 10000000 when we move on to a new stock

    
