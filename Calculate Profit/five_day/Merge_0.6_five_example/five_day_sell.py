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


# This file creates an individual csv file for each stock which displays the profit of each transaction.

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
ticker_check =""

print("Outside")
path = os.path.join("/home/ubuntu/2022_VAIV_Cho/VAIV/Yolo/Code/runs/detect/Merge_0.5_2006_5days_best2/signals")

csv_files = glob.glob(path + "/*.csv")


for file in csv_files:
    filename = open(file, "r")

    csv_file = csv.DictReader(filename)
    date = []
    label = []
    ticker = []
    close =[]
    probability = []
    five =[]
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
        five.append(col['Five'])

    print(ticker[0])
    XKRX = xcals.get_calendar("XKRX")
    pred_Dates = XKRX.sessions_in_range("2019-01-01","2021-12-31")
    pred_Dates = pred_Dates.strftime("%Y-%m-%d").tolist()
                        #  perform calculation

                        # 1 pair의 buy-sell로 pair 수익률 구하기

    for i in range(len(label)):
        #print(i)
        if "2021" in date[i] in date[i] and label[i] == 'buy': #: # If it is a 'BUY' (BUY == 1)
            if buy_check == 0:
                #print("Entered the BUY if")
            #    print("BUY: "),
                ticker_check = ticker[i]  # Records the ticker of the 'BUY' signal (종목명)

                                            # The 'BUY' index is simply -1 index of the 'BUY" signal
                                                                            # We set the buy_index -1 of the 'SELL' index.
                buy_date = date[i] # We gather info on the dates as well

                buy_price = close[i]  # We gather information on the price index as well
                                           
                sell_price = five[i]

                                            #We use this to calculate the profit of the BUY and SELL signals

                buy_probability = probability[i] #We gather information on the probability as well
                buy_date_str = str(buy_date)
                buy_date_datetime = dt.strptime(buy_date_str, '%Y-%m-%d')
                profit_only =  round( ( (float(sell_price) *0.9975) - float(buy_price) ) / float(buy_price) * 100, 3 )
                seed = round((seed * profit_only / 100)  + seed,2)
                total_profit = round(((seed - 10000000) / 10000000 )* 100,2 )                        
    
                if profit_only > 0 and sell_price != 0:
                    plus_count+=1
                    profit_sign = '+'
                    profit_plus_aggre+=profit_only
                    profit_plus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability, sell_price, profit_only, seed, profit_sign, total_profit ]

                    profit_dict.append(profit_row)

                                        
                                        #- 수익률
                elif profit_only < 0 and sell_price != 0:
                    minus_count+=1
                    profit_sign = '-'
                    profit_minus_aggre+=profit_only
                    profit_minus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability, sell_price,  profit_only, seed, profit_sign ,total_profit]

                    profit_dict.append(profit_row)
     

        if "2021" in date[i] and label[i] == 'sell': #: # If it is a 'BUY' (BUY == 1)
            if buy_check == 1:
                buy_check = 0 
                ticker_check = ticker[i]  # Records the ticker of the 'BUY' signal (종목명)

                sell_index = 1  # The 'BUY' index is simply -1 index of the 'BUY" signal
                                                                        # We set the buy_index -1 of the 'SELL' index.
                sell_date = date[i] # We gather info on the dates as well
                                        #  sell_date = old_df['Date'][trading_index] 
                sell_price = close[i]  # We gather information on the price index as well
                                        #We use this to calculate the profit of the BUY and SELL signals

                sell_probability = probability[i] #We gather information on the probability as well
                buy_date_str = str(sell_date)
                buy_date_datetime = dt.strptime(buy_date_str, '%Y-%m-%d')

                profit_only =  round( ( float(sell_price) - float(buy_price) ) / float(buy_price) * 100, 3 )
                seed = round((seed * profit_only / 100)  + seed,2)
                total_profit = round(((seed - 10000000) / 10000000 )* 100,2 )

                                        #+ 수익률
                if profit_only > 0 and sell_index == 1:
                    plus_count+=1
                    profit_sign = '+'
                    profit_plus_aggre+=profit_only
                    profit_plus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability,  sell_date, sell_price, sell_probability, profit_only, seed, profit_sign, total_profit ]

                    profit_dict.append(profit_row)

                                        
                                        #- 수익률
                elif profit_only < 0 and sell_index == 1:
                    minus_count+=1
                    profit_sign = '-'
                    profit_minus_aggre+=profit_only
                    profit_minus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability,  sell_date, sell_price, sell_probability, profit_only, seed, profit_sign ,total_profit]

                    profit_dict.append(profit_row)


                                        

                                                        
                                                            #2 buy-sell pair dataframe 생성
                

    profit_pair_df = pd.DataFrame(profit_dict,columns=['Ticker','Buy_Date','Buy_Price','Buy_Prob', 'Sell_Prob', 'Pair_Profit', 'Principal', 'Profit' ,'Total Profit'])
                                                            #3 dataframe을 csv로 생성
    profit_pair_df.sort_values(by='Buy_Date', inplace= True) # 동일한 날짜 별로 정렬, 오름차순.
    profit_pair_df.reset_index(inplace=True, drop=True)
    title = f"{ticker_check}_2019_profit.csv"
    profit_pair_df.to_csv(title,encoding='UTF-8-sig',index='False')
    profit_dict.clear()
    seed = 10000000

    