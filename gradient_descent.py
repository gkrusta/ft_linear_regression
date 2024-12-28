import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#recibe las dos listas. calcula suma al cuadrado de la diferencia de los dos
def mean_squared_error(predictions, actual_values):
    m = len(actual_values)


def visualize():
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.legend(loc='upper left')
    plt.show()
    plt.close()


#to always have data in the range (0; 1)
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]


# y = theta1 * x + theta0
def training(mileage, price):
    learning_rate = 0.0001
    theta0 = 0
    theta1 = 0
    theta1_prev = 0
    m = len(price)
    max_iterations = 100
    epsilon = 1e-6
    plt.figure(figsize = (14,11))
    #plt.scatter(mileage, price, color='blue', label='data points')
    for i in range(max_iterations):
        #y = ax + b
        predictions = [theta0 + theta1 * x for x in mileage] #first time it's 0;
        errors = [predictions - actual for predictions, actual in zip(predictions, price)]
        print(f"theta 0 (b): {theta0:.6f} \ntheta 1 (a): {theta1:f}")
        temp0 = learning_rate * 1 / m * sum(errors)
        print(f"temp0: {temp0:f}")
        temp1 = learning_rate * 1 / m * (sum([errors * mileage for errors, mileage in zip(errors, mileage)]))
        print(f"temp1: {temp1:f}")
        print("\n-----------\n")
        theta0 = (theta0 - temp0)
        theta1_prev = theta1
        theta1 = (theta1 - temp1)
        if abs(theta1 - theta1_prev) <= epsilon:
            print(f"Cover after {i + 1} iterations")
            break
    else:
        print("Rreached 100 iterations without  convergence")
    #regression_line = [theta0 + theta1 * x for x in mileage]
    #plt.plot(mileage, regression_line, label=f'Iteration {i+1}')
    #visualize()
    return(theta0, theta1)



def process_file():
    data = pd.read_csv("data.csv")
    arr_mileage = data['km']
    arr_price = data['price']
    mileage = (data['km'].tolist()) # should normalize the values
    price = (data['price'].tolist())
    estimated_intercept, estimated_slope = training(mileage, price)
    y_pred = [estimated_intercept + estimated_slope * x for x in mileage]
    min_price = min(data['price'])
    max_price = max(data['price'])
    y_pred_rescaled = [(pred * (max_price - min_price)) + min_price for pred in y_pred]
    
    plt.scatter(mileage, price, marker='o', color='red', label='Data points')
    plt.plot(mileage, y_pred_rescaled, color='blue', linestyle='dashed', label='Regression line')
    visualize()
    #print(mileage)
    #print(price)


process_file()