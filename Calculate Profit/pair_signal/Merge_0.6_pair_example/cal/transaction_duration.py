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
from datetime import datetime

buy_date = None
ticker= None
sell_date = None
profit_sign = None  


profit_dict=[]

accumulate = 0

csv_files = []

ticker = []  
duration = []


path = os.path.join("/home/ubuntu/2022_VAIV_JSPARK/YOLOv7/yolov7/Merge_0.7_pair_2006_")

csv_files = glob.glob(path + "/*.csv")

print("start")
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
    buy_date =""
    sell_date = ""

        #print(csv_file)
        
        # iterating over each row and append
        # values to empty list
    for col in csv_file:
        ticker.append(col['Ticker'])
        sell_date = col['Sell_Date']
        buy_date = col['Buy_Date']
        #  ticker = old_df['Ticker'].tolist()
        
        print(sell_date)
        print(buy_date)
        d1 = datetime.strptime(sell_date, "%Y-%m-%d")
        d2 = datetime.strptime(buy_date, "%Y-%m-%d")

        delta = d1 - d2
        print(delta.days)
        duration.append(delta.days)
        print(duration)


    #print(label)
    #break
    if len(ticker) > 0:
       #print(len(ticker)),
        print(ticker[0])







        #profit = float(principal[length])
        #accumulate += profit
        #profit_percentage = float(percentage[length])

        #profit_row= [ ticker_check, round(profit,2), round(profit_percentage,2) ]
       

    
print(duration)
print("Max: "),
print(max(duration))
print("Min: "),
print(min(duration))
print("Average"),
print( round(sum(duration) / len(duration) , 2))