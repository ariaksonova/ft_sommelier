import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas
import random
import os


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)


def draw_diagram(plot, master, slave, quality, good_threshold, bad_threshold):
    for i in range(len(master)):
        color = 'white'
        if quality[i] <= bad_threshold:
            color = 'red'
        elif quality[i] >= good_threshold:
            color = 'green'
        plot.scatter(master[i], slave[i], color=color, s=10)


def plot_scatter_matrix(wine_data, good_threshold, bad_threshold, save_plot=False):
    fig = plt.figure(figsize=(100, 100))
    for i in range(10):
        ax1 = fig.add_subplot(10, 10, i + 1)
        ax1.plot(wine_data.iloc[:, i], wine_data.iloc[:, i+1], 'ro')
    # draw_diagram(ax1, wine_data.iloc[:, 0], wine_data.iloc[:, 2], wine_data.iloc[:, -1], good_threshold, bad_threshold)
    if save_plot:
        save('plot_scatter_matrix', fmt='png')
    plt.show()


wine_data = pandas.read_csv('resources/winequality-red.csv', sep=';')
# print(wine_data, type(wine_data))
plot_scatter_matrix(wine_data, 6, 5, True)
