import plot_scatter_matrix
import perceptron

wine_data = pandas.read_csv('resources/winequality-red.csv', sep=';')
# print(wine_data, type(wine_data))
plot_scatter_matrix.plot_scatter_matrix(wine_data, 6, 5, True)
