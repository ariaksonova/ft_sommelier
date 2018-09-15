import matplotlib
import pandas
import random

def plot_scatter_matrix(wine_data, good_threshold, bad_threshold, save_plot=False):
    

wine_data = []
file = open("resources/winequality-red.csv", "r")
for line in file:
    wine_data.append(line)
plot_scatter_matrix(wine_data, 6, 5, False)



