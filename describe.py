#!/usr/bin/python

import csv
import sys
import math
import numpy as np
import pandas as pd

def compute_standard_deviation(values, mean, count):
    centered_square = 0
    for val in values:
        if np.isnan(val):
            continue
        else:
            centered_square += (val - mean)**2
    std = np.sqrt(centered_square/count)
    return std

def create_describe_df(numeric_features, data):
    info = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    df = pd.DataFrame(np.zeros(shape=(len(info), len(numeric_features))), index = info, columns = numeric_features)

    for col in df.columns:
        ordered_list = []
        _n = 0
        _total = 0
        _max = - np.inf
        _min = np.inf
        for val in data[col]:
            if np.isnan(val):
                continue
            else:
                _n += 1
                ordered_list.append(val)
                _total = _total + val
                if _max < val:
                    _max = val
                if _min > val:
                    _min = val
        ordered_list.sort()
        df[col]["Count"] = _n
        df[col]["Mean"] = _total/_n
        df[col]["Max"] = _max
        df[col]["Min"] = _min
        df[col]["Std"] = compute_standard_deviation(ordered_list, df[col]["Mean"], df[col]["Count"])
        df[col]["25%"] = ordered_list[math.ceil(_n/4) - 1]
        df[col]["50%"] = ordered_list[math.ceil(_n/2) - 1] 
        df[col]["75%"] = ordered_list[math.ceil(3*_n/4) - 1] 
    return df

def select_numeric_features(dataset):
    numeric_features = []
    for col_name in dataset.columns[2:]: # skip Index and House
        try:
            float(dataset[col_name][0])
            numeric_features.append(col_name)
        except ValueError:
            continue
    return numeric_features

def loadCsv(input):
    try:
        data = pd.read_csv(input)
    except:
        sys.exit('Csv file not found')
    return(data)

def main():

    if (len(sys.argv) != 2):
        sys.exit('Wrong number of arguments')
    input = sys.argv[1]

    data = loadCsv(input)
    numeric_features = select_numeric_features(data)
    describe_data = create_describe_df(numeric_features, data)

    print(describe_data)

if	__name__ == '__main__':
    main()
