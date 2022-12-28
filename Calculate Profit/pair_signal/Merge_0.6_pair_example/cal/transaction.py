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

path = os.path.join("[PATH_OF_CSV_FILES]") #ex) YOLO-Profit-Calculation/Calculate Profit/pair_signal/Merge_0.6_five_example

csv_files = glob.glob(path + "/*.csv")

for file in csv_files:
 
    filename = open(file, "r")
  
    csv_file = csv.DictReader(filename)
    ticker = []
    profit = 0
    principal = []
    percentage = []
    profit_percentage = 0
    num_trans = 0

        
        # iterating over each row and append
        # values to empty list
    for col in csv_file:
        ticker.append(col['Ticker'])
        
    if len(ticker) > 0:
       
        print(ticker[0])
        num_trans = len(ticker)
        ticker_check = ticker[0]

        profit_row= [ ticker_check, num_trans]
        profit_dict.append(profit_row)
       

    

                   
profit_pair_df = pd.DataFrame(profit_dict,columns=['Ticker','Number of Transactions'])
                                            #3 dataframe을 csv로 생성
profit_pair_df.reset_index(inplace=True, drop=True)
profit_pair_df.to_csv("Transaction Results.csv",encoding='UTF-8-sig',index='False')

    
