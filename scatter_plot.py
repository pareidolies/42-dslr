#!/usr/bin/python

import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from describe import select_numeric_features, loadCsv

# def plot_scatter_matrix(features, data):
#     num_features = len(features)
#     fig, axes = plt.subplots(num_features, num_features, figsize=(15, 15))

#     for i in range(num_features):
#         for j in range(num_features):
#             if i != j:
#                 ax = axes[i, j]
#                 ax.scatter(data[features[j]], data[features[i]], alpha=0.5)
#                 ax.set_xlabel(features[j])
#                 ax.set_ylabel(features[i])

#     plt.tight_layout()
#     plt.show()

def scatter_plot(numeric_features, data, first, second):
    plt.figure()
    plt.scatter(data[data["Hogwarts House"] == "Gryffindor"][first], data[data["Hogwarts House"] == "Gryffindor"][second], label='Gry', alpha = 0.5, color='r')
    plt.scatter(data[data["Hogwarts House"] == "Ravenclaw"][first], data[data["Hogwarts House"] == "Ravenclaw"][second], label='Rav', alpha = 0.5, color='b')
    plt.scatter(data[data["Hogwarts House"] == "Slytherin"][first], data[data["Hogwarts House"] == "Slytherin"][second], label='Sly', alpha = 0.5, color='g')
    plt.scatter(data[data["Hogwarts House"] == "Hufflepuff"][first], data[data["Hogwarts House"] == "Hufflepuff"][second], label='Huf', alpha = 0.5, color='y')
    plt.legend()
    plt.title("Correlated features")
    plt.xlabel("Astronomy")
    plt.ylabel("Defense Against the Dark Arts")
    plt.show()

def main():

    if (len(sys.argv) != 2):
        sys.exit('Wrong number of arguments')
    input = sys.argv[1]

    data = loadCsv(input)

    numeric_features = select_numeric_features(data)
    scatter_plot(numeric_features, data, 'Astronomy', 'Defense Against the Dark Arts')

if	__name__ == '__main__':
    main()
