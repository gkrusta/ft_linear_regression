import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
from utils import save_parameters, read_file


def visualize():
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.legend(loc='upper right')
    plt.show()
    plt.close()


#to always have data in the range (0; 1)
def normalize(mileage, mileage_mean, mileage_std):
    return [(x - mileage_mean) / mileage_std for x in mileage]


# y = theta1 * x + theta0
def training(mileage, price):
    learning_rate = 0.02
    theta0 = 0
    theta1 = 0
    theta1_prev = 0
    m = len(price)
    max_iterations = 1200
    epsilon = 1e-3
    plt.figure(figsize = (14,11))

    for i in range(max_iterations):
        #y = ax + b
        predictions = [theta0 + theta1 * x for x in mileage] #first time it's 0;
        errors = [predictions - actual for predictions, actual in zip(predictions, price)]
        print(f"theta 0 (b): {theta0:.6f} \ntheta 1 (a): {theta1:f}")
        temp0 = learning_rate * (1 / m) * sum(errors)
        print(f"temp0: {temp0:f}")
        temp1 = learning_rate * (1 / m) * (sum(errors * mileage for errors, mileage in zip(errors, mileage)))
        print(f"temp1: {temp1:f}")
        print("\n-----------\n")
        theta0 -= temp0
        theta1 -= temp1
        print("DIF: ", abs(temp0), abs(temp1))

        if abs(temp0) < epsilon and abs(temp1) < epsilon:
            print(f"Cover after {i + 1} iterations")
            break

    else:
        print(f"Rreached {max_iterations} iterations without convergence")

    return(theta0, theta1)


def revert_normalize(estimated_intercept, estimated_slope, mileage_mean, mileage_std):
    """
    Reverts normalized regression parameters to the original scale.
    
    Parameters:
        theta0 (float): Intercept from normalized regression.
        theta1 (float): Slope from normalized regression.
        mileage_mean (float): Mean of the original mileage data.
        mileage_std (float): Standard deviation of the original mileage data.
    """
    estimated_intercept_original = estimated_intercept - (estimated_slope * mileage_mean / mileage_std)
    estimated_slope_original = estimated_slope / mileage_std

    return estimated_intercept_original, estimated_slope_original


def process_file():
    mileage, price = read_file()
    mileage_mean = np.mean(mileage)
    mileage_std = np.std(mileage)
    mileage_normalized = normalize(mileage, mileage_mean, mileage_std)

    print(mileage)
    print(price)
    estimated_intercept, estimated_slope = training(mileage_normalized, price)
    intercept, slope = revert_normalize(estimated_intercept, estimated_slope, mileage_mean, mileage_std)
    regression_line = [intercept + slope * x for x in mileage]

    plt.scatter(mileage, price, marker='o', color='red', label='Data points')
    plt.plot(mileage, regression_line, color='blue', linestyle='dashed', label='Regression line')
    visualize()
    return intercept, slope


def main():
    try:
        intercept, slope = process_file()
        save_parameters(intercept, slope)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
