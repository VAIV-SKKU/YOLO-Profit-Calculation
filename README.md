# YOLO-Profit-Calculation
Calculates the yearly profits from the results of YOLO's detect model


## Getting Started

### Clone Repository

```
https://github.com/VAIV-SKKU/YOLO-Profit-Calculation.git

```

### Prerequisite

```
pip install -r requirements.txt

```
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

```
runs
└── detect
      └── [DUMMY_RUN]
            ├── images
            ├── labels  
            ├── signals
                 ├── 000020.csv
                 └── ...

```

1. Insert the address of the 'signal' folder which contains the detected csv files to the path in pair_csv_create.py or five_day_sell.py.
```
ex) path = os.path.join("[DETECT_CSV_FILE_PATH]")
```
2. Run the file. This will create the transaction list of each individual stock into a csv format.

```
python five_day_sell.py

python pair_csv_create.py
```

3. Copy the address of the folder containing the recently created csv files and go into the 'cal' folder and insert the copied address into the path in profit_compare.py.  
```
ex) path = os.path.join("[CSV_FILE_PATH]")
```
4. Run the file. This would create a csv file containing the total profits of each individual stock. 

```
python profit_compare.py
```

5. Copy the address of that csv file and insert it into profit_average.py

```
filename = open("[PATH_OF_PROFIT_COMPARE_CSV_FILE]", "r")

```
6. Run the file

```
python profit_average.py
```







