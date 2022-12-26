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

# This file calculates the average profit of all of the stocks in a folder.

buy_date = None
ticker= None
sell_date = None
profit_sign = None  


profit_dict=[]

accumulate = 0

csv_files = []

ticker = []    


# We must first run the profit_compare.py file and use the csv file created from that file and input it in the following filename.

filename = open("/home/ubuntu/2022_VAIV_JSPARK/YOLOv7/yolov7/Merge_0.6_pair_2006_best/cal/2019Accumulated Profit Results.csv", "r")

                

csv_file = csv.DictReader(filename)
ticker = []
profit = 0
principal = []
percentage = []
percentage_float = []
average_profit_percentage = 0

        
        # iterating over each row and append
        # values to empty list
for col in csv_file:
    ticker.append(col['Ticker'])
    percentage.append(col['Profit Percentage'])

    

if len(ticker) > 0:

    length = len(percentage) - 1

    for i in range(len(percentage)):
        percentage_float.append(float(percentage[i]))

    print(float(sum(percentage_float)))
    print(float(len(percentage_float)))
    average_profit_percentage = float(sum(percentage_float)) / float(len(percentage_float))

    profit_row= [round(average_profit_percentage,2) ]
    profit_dict.append(profit_row)
       

    

                   
profit_pair_df = pd.DataFrame(profit_dict,columns=['Profit Percentage Average'])
                                            #3 dataframe을 csv로 생성
profit_pair_df.reset_index(inplace=True, drop=True)
profit_pair_df.to_csv("Average Accumulated Profit Results.csv",encoding='UTF-8-sig',index='False') # Returns the average in a csv file
