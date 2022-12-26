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
#print(directory)
#print("path:" + path)
#path = "/home/ubuntu/2022_VAIV_Dataset/Yolo1/Code/yolov7/runs/detect/stock_02/signals/"
#path = "/home/ubuntu/2022_VAIV_HyunJoon/yolov5/runs/detect/test_50/signals/"
csv_files = glob.glob(path + "/*.csv")
#old_df  = pd.read_csv("/home/ubuntu/2022_VAIV_Dataset/Yolo1/Code/yolov7/runs/detect/stock_02/signals/",index_col=0) #  마지막 날  buy-sell matching csv 
#old_df.reset_index(inplace=True, drop=True)
#print("length of csv list")

#print("csv_files:" + str(csv_files))

for file in csv_files:
 #   print(file)
    filename = open(file, "r")
  #  print(filename)

                
        #old_df = open(file, 'r')
        #  old_df = pd.read_csv(file ,index_col=0) #  마지막 날  buy-sell matching csv 
                #    old_df.reset_index(inplace=True, drop=True)
 #   print("We opened the file")
    csv_file = csv.DictReader(filename)
    date = []
    label = []
    ticker = []
    close =[]
    probability = []
    five =[]
    seed = 10000000
    buy_check = 0
        #print(csv_file)
        
        # iterating over each row and append
        # values to empty list
    for col in csv_file:
        ticker.append(col['Ticker'])
        date.append(col['Date'])
        label.append(col['Label'])
        close.append(col['Close'])
        probability.append(col['Probability'])
        five.append(col['Five'])
        #  ticker = old_df['Ticker'].tolist()
    #print(label)
    #break
    print(ticker[0])
    XKRX = xcals.get_calendar("XKRX")
    pred_Dates = XKRX.sessions_in_range("2019-01-01","2021-12-31")
    pred_Dates = pred_Dates.strftime("%Y-%m-%d").tolist()
                        #  perform calculation

                        # 1 pair의 buy-sell로 pair 수익률 구하기
                #  print(trading_index)
                # print(old_df['Label'][0])
    #print(i)
    #print(label[i] == "BUY")
#    print(label[i])
    for i in range(len(label)):
        #print(i)
        if "2021" in date[i] or "2020" in date[i] or "2019" in date[i] and label[i] == 'buy': #: # If it is a 'BUY' (BUY == 1)
            if buy_check == 0:
                #print("Entered the BUY if")
            #    print("BUY: "),
                ticker_check = ticker[i]  # Records the ticker of the 'BUY' signal (종목명)

                                            # buy_index = trading_index # The 'BUY' index is simply -1 index of the 'BUY" signal
                                                                            # We set the buy_index -1 of the 'SELL' index.
                buy_date = date[i] # We gather info on the dates as well
                                            #  sell_date = old_df['Date'][trading_index] 
            #    print(buy_date),

                buy_price = close[i]  # We gather information on the price index as well
                                            #  sell_price = old_df['Close'][trading_index]
                sell_price = five[i]

                                            #We use this to calculate the profit of the BUY and SELL signals
             #   print(buy_price),

                buy_probability = probability[i] #We gather information on the probability as well
                                            #  sell_probability = old_df['Probability'][trading_index]
            #    print(buy_probability),
                buy_date_str = str(buy_date)
                                            #  sell_date_str = str(sell_date)
           #     print(buy_date_str),
                buy_date_datetime = dt.strptime(buy_date_str, '%Y-%m-%d')
                                        # sell_date_datetime = dt.strptime(sell_date_str, "%Y-%m-%d")
                profit_only =  round( ( (float(sell_price) *0.9975) - float(buy_price) ) / float(buy_price) * 100, 3 )
                seed = round((seed * profit_only / 100)  + seed,2)
                total_profit = round(((seed - 10000000) / 10000000 )* 100,2 )                        
          #      print(buy_date_datetime)                        
                                        #  profit_co =  round( ( sell_price*0.9975 - buy_price ) / buy_price * 100 , 3) 
                                        # profit_co = round( ( ( sell_price*0.9975 - buy_price ) / buy_price * 100 )/ np.busday_count(buy_date_datetime.date(), sell_date_datetime.date(), "1111100" )  , 3)
                                        #  profit_only =  round( ( sell_price - buy_price ) / buy_price * 100, 3 )
                                        #profit_only = round( ( sell_price - buy_price ) / buy_price * 100 /  np.busday_count(buy_date_datetime.date(), sell_date_datetime.date(), "1111100" ) , 3)
        #print("Exited BUY if ")
                if profit_only > 0 and sell_price != 0:
                    plus_count+=1
                    profit_sign = '+'
                    profit_plus_aggre+=profit_only
                    profit_plus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability, sell_price, profit_only, seed, profit_sign, total_profit ]
                    #print("profit_row: "),
                    #print(profit_row)
                    profit_dict.append(profit_row)
                    #print("profit_dict: "),
                    #print(profit_dict)
                                        
                                        #- 수익률
                elif profit_only < 0 and sell_price != 0:
                    minus_count+=1
                    profit_sign = '-'
                    profit_minus_aggre+=profit_only
                    profit_minus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability, sell_price,  profit_only, seed, profit_sign ,total_profit]
                    #print("profit_row: "),
                    #print(profit_row)
                    profit_dict.append(profit_row)
                    #print("profit_dict: "),
                    #print(profit_dict)        

        if "2021" in date[i] or "2020" in date[i] or "2019" in date[i] and label[i] == 'sell': #: # If it is a 'BUY' (BUY == 1)
            if buy_check == 1:
              #  print("SELL: ")
                buy_check = 0 
                #print("Entered the SELL if")
                ticker_check = ticker[i]  # Records the ticker of the 'BUY' signal (종목명)

                sell_index = 1 # The 'BUY' index is simply -1 index of the 'BUY" signal
                                                                        # We set the buy_index -1 of the 'SELL' index.
                sell_date = date[i] # We gather info on the dates as well
                                        #  sell_date = old_df['Date'][trading_index] 
               # print(sell_date),
                sell_price = close[i]  # We gather information on the price index as well
                                        #  sell_price = old_df['Close'][trading_index]
               # print(sell_price),
                                        #We use this to calculate the profit of the BUY and SELL signals

                sell_probability = probability[i] #We gather information on the probability as well
                                        #  sell_probability = old_df['Probability'][trading_index]
               # print(sell_probability),
                buy_date_str = str(sell_date)
                                        #  sell_date_str = str(sell_date)
              #  print(buy_date_str),
                buy_date_datetime = dt.strptime(buy_date_str, '%Y-%m-%d')
                                        # sell_date_datetime = dt.strptime(sell_date_str, "%Y-%m-%d")
                #profit_co = round( ( ( int(sell_price)*0.9975 - int(buy_price) ) / int(buy_price) * 100 )/ np.busday_count(buy_date_datetime.date(), sell_date_datetime.date(), "1111100" )  , 3)
                #print(buy_date_datetime),
                profit_only =  round( ( float(sell_price) - float(buy_price) ) / float(buy_price) * 100, 3 )
                seed = round((seed * profit_only / 100)  + seed,2)
                total_profit = round(((seed - 10000000) / 10000000 )* 100,2 )
                #print("profit: "),
                #print(profit_only)
                                        #+ 수익률
                if profit_only > 0 and sell_index == 1:
                    plus_count+=1
                    profit_sign = '+'
                    profit_plus_aggre+=profit_only
                    profit_plus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability,  sell_date, sell_price, sell_probability, profit_only, seed, profit_sign, total_profit ]
                    #print("profit_row: "),
                    #print(profit_row)
                    profit_dict.append(profit_row)
                    #print("profit_dict: "),
                    #print(profit_dict)
                                        
                                        #- 수익률
                elif profit_only < 0 and sell_index == 1:
                    minus_count+=1
                    profit_sign = '-'
                    profit_minus_aggre+=profit_only
                    profit_minus_aggre_co+=profit_co
                    sell_index = 0
                    profit_row= [ ticker_check, buy_date, buy_price, buy_probability,  sell_date, sell_price, sell_probability, profit_only, seed, profit_sign ,total_profit]
                    #print("profit_row: "),
                    #print(profit_row)
                    profit_dict.append(profit_row)
                    #print("profit_dict: "),
                    #print(profit_dict)

                                        

                                                        
                                        #2 buy-sell pair dataframe 생성
                
        #print("About to break")
    #print("length: ", len(label))
    profit_pair_df = pd.DataFrame(profit_dict,columns=['Ticker','Buy_Date','Buy_Price','Buy_Prob', 'Sell_Prob', 'Pair_Profit', 'Principal', 'Profit' ,'Total Profit'])
                                            #3 dataframe을 csv로 생성
    profit_pair_df.sort_values(by='Buy_Date', inplace= True) # 동일한 날짜 별로 정렬, 오름차순.
    profit_pair_df.reset_index(inplace=True, drop=True)
    title = f"{ticker_check}_2019_profit.csv"
    profit_pair_df.to_csv(title,encoding='UTF-8-sig',index='False')
    profit_dict.clear()
    seed = 10000000
    #if counter == 1:
        #break
    #counter += 1
    