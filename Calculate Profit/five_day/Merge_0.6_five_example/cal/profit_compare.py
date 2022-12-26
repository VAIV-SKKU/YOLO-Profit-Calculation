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

# This file calculates the total profit of each individual stock during a certain duration. 

buy_date = None
ticker= None
sell_date = None
profit_sign = None  


profit_dict=[]

accumulate = 0

csv_files = []

ticker = []    


# We put in the folder that contains the csv files that we want to calculate.

path = os.path.join("/home/ubuntu/2022_VAIV_JSPARK/YOLOv7/yolov7/Merge_0.6_pair_example")

csv_files = glob.glob(path + "/*.csv")

for file in csv_files:
    filename = open(file, "r")

    csv_file = csv.DictReader(filename)
    ticker = []
    profit = 0
    principal = []
    percentage = []
    profit_percentage = 0

        
        # iterating over each row and append
        # values to empty list
    for col in csv_file:
        ticker.append(col['Ticker'])
        principal.append(col['Principal'])
        percentage.append(col['Total Profit'])

    if len(ticker) > 0:
        print(ticker[0])
        ticker_check = ticker[0]
        length = len(principal) - 1

        profit = float(principal[length])
        accumulate += profit
        profit_percentage = float(percentage[length])

        profit_row= [ ticker_check, round(profit,2), round(profit_percentage,2) ]
        profit_dict.append(profit_row)
       

    

                   
profit_pair_df = pd.DataFrame(profit_dict,columns=['Ticker','Total Profit', 'Profit Percentage'])
                                            #3 dataframe을 csv로 생성
profit_pair_df.reset_index(inplace=True, drop=True)
profit_pair_df.to_csv("2019Accumulated Profit Results.csv",encoding='UTF-8-sig',index='False')

    