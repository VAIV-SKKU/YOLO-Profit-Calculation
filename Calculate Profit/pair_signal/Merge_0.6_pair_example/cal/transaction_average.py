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

#path = os.path.join("/home/ubuntu/2022_VAIV_JSPARK/YOLOv7/yolov7/calculate_profit/KOSPI Accumulated Profit Results.csv")

#csv_files = glob.glob(path + "/*.csv")


 #   print(file)
filename = open("/home/ubuntu/2022_VAIV_JSPARK/YOLOv7/yolov7/Merge_0.7_pair_2006_best/cal/Transaction Results.csv", "r")
  #  print(filename)

                
        #old_df = open(file, 'r')
        #  old_df = pd.read_csv(file ,index_col=0) #  마지막 날  buy-sell matching csv 
                #    old_df.reset_index(inplace=True, drop=True)
 #   print("We opened the file")
csv_file = csv.DictReader(filename)
ticker = []
profit = 0
transaction = []
percentage = []
transaction_float = []
transaction_average = 0

        #print(csv_file)
        
        # iterating over each row and append
        # values to empty list
for col in csv_file:
    ticker.append(col['Ticker'])
        #principal.append(col['Principal'])
    transaction.append(col['Number of Transactions'])

    
        #  ticker = old_df['Ticker'].tolist()
    #print(label)
    #break
if len(ticker) > 0:
       #print(len(ticker)),
    #print(ticker[0])
    #ticker_check = ticker[0]
    #length = len(transaction) - 1

    #profit = float(principal[length])
    #accumulate += profit
    for i in range(len(transaction)):
        transaction_float.append(float(transaction[i]))

    print(float(sum(transaction_float)))
   # print(float(len(percentage_float)))
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