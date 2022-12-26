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

path = os.path.join("/home/ubuntu/2022_VAIV_JSPARK/YOLOv7/yolov7/Merge_0.7_pair_2006_best")

csv_files = glob.glob(path + "/*.csv")

for file in csv_files:
 #   print(file)
    filename = open(file, "r")
  #  print(filename)

                
        #old_df = open(file, 'r')
        #  old_df = pd.read_csv(file ,index_col=0) #  마지막 날  buy-sell matching csv 
                #    old_df.reset_index(inplace=True, drop=True)
 #   print("We opened the file")
    csv_file = csv.DictReader(filename)
    ticker = []
    profit = 0
    principal = []
    percentage = []
    profit_percentage = 0
    num_trans = 0

        #print(csv_file)
        
        # iterating over each row and append
        # values to empty list
    for col in csv_file:
        ticker.append(col['Ticker'])
        #principal.append(col['Principal'])
        #percentage.append(col['Total Profit Percentage'])
        #  ticker = old_df['Ticker'].tolist()
    #print(label)
    #break
    if len(ticker) > 0:
       #print(len(ticker)),
        print(ticker[0])
        num_trans = len(ticker)
        ticker_check = ticker[0]

        profit_row= [ ticker_check, num_trans]
        profit_dict.append(profit_row)
       

    

                   
profit_pair_df = pd.DataFrame(profit_dict,columns=['Ticker','Number of Transactions'])
                                            #3 dataframe을 csv로 생성
#profit_pair_df.sort_values(by='Buy_Date', inplace= True) # 동일한 날짜 별로 정렬, 오름차순.
profit_pair_df.reset_index(inplace=True, drop=True)
profit_pair_df.to_csv("Transaction Results.csv",encoding='UTF-8-sig',index='False')
    #if counter == 1:
        #break
    #counter += 1
    