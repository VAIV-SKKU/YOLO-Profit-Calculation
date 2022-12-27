# YOLO-Profit-Calculation
Calculates the yearly profits from the results of YOLO's detect model


## Calculating Profit

There are two options in calculating the profit's from the YOLOv7 detection model- profits of five days later and profits of buy/sell pairs.


## File Structure

```
.
├── Calculate Profit/
│    ├── five_day/
|         ├── Merge_0.6_five_example
|    ├── pair_signal/
│         ├── Merge_0.6_pair_example

```
## How to Calculate Average Profit

1. Insert the address of the folder containing the detected csv files to the path in pair_csv_create.py / five_day_sell.py.
```
ex) path = os.path.join("/home/ubuntu/2022_VAIV_Cho/VAIV/Yolo/Code/runs/detect/Merge_0.7_2006_best_pair2/signals")
```
2. Run the file

3. Copy the address of the folder containing the recently created csv files and go into the 'cal' folder and insert it into the path in profit_compare.py.  
```
ex) path = os.path.join("/home/ubuntu/2022_VAIV_JSPARK/YOLOv7/yolov7/Merge_0.7_pair_2006_best")
```
4. Run the file. This would create a csv file containing the total profits of each individual stock. 

5. Copy the address of that csv file and insert it into profit_average.py





