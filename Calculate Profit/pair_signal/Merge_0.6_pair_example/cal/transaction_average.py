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

buy_date = None
ticker= None
sell_date = None
profit_sign = None  


profit_dict=[]

accumulate = 0

csv_files = []

ticker = []    

filename = open("[PATH_OF_TRANSACTION_CSV_FILE]", "r") # ex) YOLO-Profit-Calculation/Calculate Profit/pair_signal/Merge_0.6_five_example/cal/Transaction Result.csv

csv_file = csv.DictReader(filename)
ticker = []
profit = 0
transaction = []
percentage = []
transaction_float = []
transaction_average = 0

        
        # iterating over each row and append
        # values to empty list
for col in csv_file:
    ticker.append(col['Ticker'])
    transaction.append(col['Number of Transactions'])

    
if len(ticker) > 0:
    for i in range(len(transaction)):
        transaction_float.append(float(transaction[i]))

    print(float(sum(transaction_float)))
    transaction_average = float(sum(transaction_float)) / float(len(transaction_float))

    profit_row= [round(transaction_average,2) ]
    profit_dict.append(profit_row)
       

    

                   
profit_pair_df = pd.DataFrame(profit_dict,columns=['Average Transaction'])
                                            #3 dataframe을 csv로 생성
#profit_pair_df.sort_values(by='Buy_Date', inplace= True) # 동일한 날짜 별로 정렬, 오름차순.
profit_pair_df.reset_index(inplace=True, drop=True)
profit_pair_df.to_csv("2019TEST_Merge_0.7 Average Transaction Results.csv",encoding='UTF-8-sig',index='False')
    #if counter == 1:
        #break
    #counter += 1
