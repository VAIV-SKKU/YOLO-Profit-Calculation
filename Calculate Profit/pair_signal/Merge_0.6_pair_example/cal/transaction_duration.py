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


path = os.path.join("[PATH_OF_CSV_FILE]") # ex) YOLO-Profit-Calculation/Calculate Profit/pair_signal/Merge_0.6_pair_example

csv_files = glob.glob(path + "/*.csv")

print("start")
for file in csv_files:
    filename = open(file, "r")

                
    csv_file = csv.DictReader(filename)
    ticker = []
    profit = 0
    principal = []
    percentage = []
    profit_percentage = 0
    buy_date =""
    sell_date = ""

        
        # iterating over each row and append
        # values to empty list
    for col in csv_file:
        ticker.append(col['Ticker'])
        sell_date = col['Sell_Date']
        buy_date = col['Buy_Date']
        
        print(sell_date)
        print(buy_date)
        d1 = datetime.strptime(sell_date, "%Y-%m-%d")
        d2 = datetime.strptime(buy_date, "%Y-%m-%d")

        delta = d1 - d2
        print(delta.days)
        duration.append(delta.days)
        print(duration)


    if len(ticker) > 0:
        print(ticker[0])
       

    
print(duration)
print("Max: "),
print(max(duration))
print("Min: "),
print(min(duration))
print("Average"),
print( round(sum(duration) / len(duration) , 2))
