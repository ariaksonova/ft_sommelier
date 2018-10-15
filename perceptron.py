import pandas

def activation_function():
    pass

def proceed(wine_data, epoch, rate):
    wine_data = wine_data[wine_data['quality'] >= 8 or wine_data['quality'] <= 3]