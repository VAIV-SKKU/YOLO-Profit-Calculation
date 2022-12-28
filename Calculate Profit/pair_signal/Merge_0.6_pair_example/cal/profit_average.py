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

filename = open("[PATH_OF_CSV_FILE", "r") # ex) YOLO-Profit-Calculation/Calculate Profit/pair_signal/Merge_0.6_five_example/cal/2019Accumulated Profit Results.csv

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
profit_pair_df.to_csv("2019_Average Accumulated Profit Results.csv",encoding='UTF-8-sig',index='False')
