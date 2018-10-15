import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas
import random
import os


left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height

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
        plot.scatter(master[i], slave[i], color=color, s=1)


def plot_scatter_matrix(wine_data, good_threshold, bad_threshold, save_plot=False):
    fig = plt.figure(figsize=(100, 100))
    wine_good = wine_data[wine_data['quality'] >= good_threshold]
    wine_bad = wine_data[wine_data['quality'] <= bad_threshold]
    length = len(wine_data.columns) - 1
    for i in range(length):
        ax = fig.add_subplot(length, length, (length+1)*i+1)
        ax.text(0.5 * (left + right), 0.5 * (bottom + top), wine_data.columns[i], horizontalalignment='center', verticalalignment='center', fontsize=20, color='black', transform=ax.transAxes)
        for j in range(i+1, length):
            ax1 = fig.add_subplot(length, length, (i*length+j+1))
            ax1.plot(wine_bad.iloc[:, j], wine_bad.iloc[:, i], 'ro', wine_good.iloc[:, j], wine_good.iloc[:, i], 'go')
            ax2 = fig.add_subplot(length, length, (j * length + i + 1))
            ax2.plot(wine_bad.iloc[:, i], wine_bad.iloc[:, j], 'ro', wine_good.iloc[:, i], wine_good.iloc[:, j], 'go')
    if save_plot:
        save('plot_scatter_matrix', fmt='png')
    plt.show()