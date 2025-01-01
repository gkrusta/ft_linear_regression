import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def visualize():
    plt.xlabel('Mileage (km)')
    plt.ylabel('Price (€)')
    plt.legend(loc='upper left')
    plt.show()
    plt.close()

# Normalize mileage to (0, 1) or z-score
def normalize(mileage):
    mileage_mean = np.mean(mileage)
    mileage_std = np.std(mileage)
    return [(x - mileage_mean) / mileage_std for x in mileage], mileage_mean, mileage_std

# Revert normalized mileage back to original scale
def revert_normalize(normalized_mileage, mileage_mean, mileage_std):
    return [(x * mileage_std) + mileage_mean for x in normalized_mileage]

# Train linear regression
def training(mileage, price):
    learning_rate = 0.01
    theta0 = 0
    theta1 = 0
    m = len(price)
    max_iterations = 1000
    epsilon = 1e-5

    for i in range(max_iterations):
        # Calculate predictions
        predictions = [theta0 + theta1 * x for x in mileage]
        errors = [pred - actual for pred, actual in zip(predictions, price)]

        # Calculate gradients
        temp0 = learning_rate * (1 / m) * sum(errors)
        temp1 = learning_rate * (1 / m) * sum(error * x for error, x in zip(errors, mileage))

        # Update parameters
        theta0 -= temp0
        theta1 -= temp1

        # Check for convergence
        if abs(temp1) < epsilon:
            print(f"Converged after {i + 1} iterations")
            break
    else:
        print("Reached maximum iterations without convergence")

    return theta0, theta1

# Process the CSV file and plot
def process_file():
    # Load data
    data = pd.read_csv("data.csv")
    mileage = data['km'].tolist()
    price = data['price'].tolist()

    # Normalize mileage
    mileage_normalized, mileage_mean, mileage_std = normalize(mileage)

    # Train the model
    estimated_intercept, estimated_slope = training(mileage_normalized, price)

    # Adjust coefficients to original mileage scale
    estimated_slope_original = estimated_slope / mileage_std
    estimated_intercept_original = estimated_intercept - (estimated_slope * mileage_mean / mileage_std)

    # Generate predictions for the regression line
    regression_line = [estimated_intercept_original + estimated_slope_original * x for x in mileage]

    # Plot original data points and regression line
    plt.scatter(mileage, price, marker='o', color='red', label='Data points')
    plt.plot(mileage, regression_line, color='blue', linestyle='dashed', label='Regression line')

    visualize()

process_file()
