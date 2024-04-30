#!/usr/bin/python

import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from describe import select_numeric_features

def loadCsv(input):
    try:
        data = pd.read_csv(input)
    except:
        sys.exit('Csv file not found')
    return(data)

def plot_hist(numeric_features, data):
    num_features = len(numeric_features)
    num_rows = math.ceil(num_features / 3)
    fig, axes = plt.subplots(num_rows, 3, figsize=(15, 4*num_rows))

    for i, col in enumerate(numeric_features):
        row_idx = i // 3  
        col_idx = i % 3   
        ax = axes[row_idx, col_idx] if num_rows > 1 else axes[col_idx]
        
        ax.hist(data[data["Hogwarts House"] == "Gryffindor"][col], bins=25, alpha=0.5, label='Gry', color='r')
        ax.hist(data[data["Hogwarts House"] == "Ravenclaw"][col], bins=25, alpha=0.5, label='Rav', color='b')
        ax.hist(data[data["Hogwarts House"] == "Slytherin"][col], bins=25, alpha=0.5, label='Sly', color='g')
        ax.hist(data[data["Hogwarts House"] == "Hufflepuff"][col], bins=25, alpha=0.5, label='Huf', color='y')
        ax.legend(loc='upper right')
        ax.set_title(col)

    plt.subplots_adjust(wspace=0.1, hspace=0.6)
    plt.show()

def main():

    if (len(sys.argv) != 2):
        sys.exit('Wrong number of arguments')
    input = sys.argv[1]

    data = loadCsv(input)

    numeric_features = select_numeric_features(data)
    plot_hist(numeric_features, data)

if	__name__ == '__main__':
    main()
