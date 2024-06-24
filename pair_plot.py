#!/usr/bin/python

import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seaborn
from describe import loadCsv

def select_numeric_features(data):
    numeric_features = data.select_dtypes(include=['number']).columns.tolist()
    if "Hogwarts House" in data.columns:
        numeric_features.append("Hogwarts House")
    return numeric_features

# still need to improve layout
def pair_plot(numeric_features, data):
    pair_plot_fig = seaborn.pairplot(data[numeric_features], hue="Hogwarts House", 
                     palette={"Gryffindor": "r", "Ravenclaw": "b", "Slytherin": "g", "Hufflepuff": "y"}, 
                     diag_kind="kde", 
                     markers=["o", "s", "D", "P"])
    pair_plot_fig.fig.subplots_adjust(bottom=0.05) 
    plt.show()

def main():

    if (len(sys.argv) != 2):
        sys.exit('Wrong number of arguments')
    input = sys.argv[1]

    data = loadCsv(input)

    numeric_features = select_numeric_features(data)
    pair_plot(numeric_features, data)

if	__name__ == '__main__':
    main()
