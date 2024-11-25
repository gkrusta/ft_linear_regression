import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#recibe las dos listas. calcula suma al cuadrado de la diferencia de los dos
def mean_squared_error(predictions, actual_values):
    m = len(actual_values)


# y = theta1 * x + theta0
def training(mileage, price):
    learning_rate = 0.001
    theta0 = 0
    theta1 = 0
    m = len(price)
    i = 0

    while (i < 10):
        predictions = [theta0 + theta1 * x for x in mileage]#first time it's 0
        errors = [predictions - actual for predictions, actual in zip(predictions, price)]
        print("Errors:", errors)
        temp0 = learning_rate * 1 / m * sum(errors)
        print("temp0:", temp0)
        temp1 = learning_rate * 1 / m * (sum([errors * mileage for errors, mileage in zip(errors, mileage)]))
        print("temp1:", temp1)
        theta0 = theta0 - temp0
        theta1 = theta1 - temp1
        i += 1



def process_file():
    data = pd.read_csv("data.csv")
    arr_mileage = data['km']
    arr_price = data['price']
    mileage = arr_mileage.tolist()
    price = arr_price.tolist()
    training(mileage, price)
    #print(mileage)
    #print(price)


process_file()