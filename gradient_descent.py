import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#recibe las dos listas. calcula suma al cuadrado de la diferencia de los dos
def mean_squared_error(predictions, actual_values):
    m = len(actual_values)


def visualize():
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.legend(loc='upper right')
    plt.show()
    plt.close()


#to always have data in the range (0; 1)
def normalize(mileage):
    mileage_mean = np.mean(mileage)
    mileage_std = np.std(mileage)
    return [(x - mileage_mean) / mileage_std for x in mileage]


# y = theta1 * x + theta0
def training(mileage, price):
    learning_rate = 0.000001
    theta0 = 0
    theta1 = 0
    theta1_prev = 0
    m = len(price)
    max_iterations = 100
    epsilon = 1e-3
    plt.figure(figsize = (14,11))

    for i in range(max_iterations):
        #y = ax + b
        predictions = [theta0 + theta1 * x for x in mileage] #first time it's 0;
        errors = [predictions - actual for predictions, actual in zip(predictions, price)]
        print(f"theta 0 (b): {theta0:.6f} \ntheta 1 (a): {theta1:f}")
        temp0 = learning_rate * 1 / m * sum(errors)
        print(f"temp0: {temp0:f}")
        temp1 = learning_rate * 1 / m * (sum(errors * mileage for errors, mileage in zip(errors, mileage)))
        print(f"temp1: {temp1:f}")
        print("\n-----------\n")
        new_theta0 = theta0 - temp0
        new_theta1 = theta1 - temp1
        print("DIF: ", abs(theta1 - theta1_prev))

        if abs(new_theta0 - theta0) < epsilon and abs(new_theta1 - theta1) < epsilon:
            print(f"Cover after {i + 1} iterations")
            break

        theta0, theta1 = new_theta0, new_theta1
    else:
        print("Rreached 100 iterations without  convergence")

    return(theta0, theta1)

def revert_normalize(mileage):
    mileage_mean = np.mean(mileage)
    mileage_std = np.std(mileage)
    return [(x * mileage_std) / mileage_mean for x in mileage]

def process_file():
    data = pd.read_csv("data.csv")
    mileage = normalize(data['km'].tolist())
    price = (data['price'].tolist())

    print(mileage)
    print(price)
    estimated_intercept, estimated_slope = training(mileage, price)
    y_pred = [estimated_intercept + estimated_slope * x for x in mileage]
    min_price = min(data['price'])
    max_price = max(data['price'])
    y_pred_rescaled = [(pred * (max_price - min_price)) + min_price for pred in y_pred]
    #y_pred_rescaled = revert_normalize()
    plt.scatter(mileage, price, marker='o', color='red', label='Data points')
    plt.plot(mileage, y_pred_rescaled, color='blue', linestyle='dashed', label='Regression line')
    visualize()


process_file()