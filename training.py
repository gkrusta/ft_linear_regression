import sys
import numpy as np
from utils import save_parameters, read_file, visualize


def normalize(mileage, mileage_mean, mileage_std):
    """
    Normalizes the input mileage data using the z-score normalization formula.
    It ensures all features are on a similar scale,
    leading to faster and more stable optimization.
    """
    return [(x - mileage_mean) / mileage_std for x in mileage]


def training(mileage, price):
    """
    This function performs linear regression training using
    the gradient descent algorithm to optimize the parameters
    theta0 (intercept) and theta1 (slope).
    y = theta1 * x + theta0
    """
    learning_rate = 0.02
    theta0 = 0
    theta1 = 0
    theta1_prev = 0
    m = len(price)
    max_iterations = 1000
    epsilon = 1e-3

    for i in range(max_iterations):
        predictions = [theta0 + theta1 * x for x in mileage]
        errors = [predictions - actual for predictions, actual in zip(predictions, price)]
        temp0 = learning_rate * (1 / m) * sum(errors)
        temp1 = learning_rate * (1 / m) * (sum(errors * mileage for errors, mileage in zip(errors, mileage)))
        theta0 -= temp0
        theta1 -= temp1

        if abs(temp0) < epsilon and abs(temp1) < epsilon:
            print(f"Convergence after {i + 1} iterations")
            break

    else:
        print(f"Reached {max_iterations} iterations without convergence")

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


def main():
    try:
        mileage, price = read_file()
        if len(sys.argv) > 1 and sys.argv[1] == "-d":
            visualize(mileage, price)
        elif len(sys.argv) == 1:
            mileage_mean = np.mean(mileage)
            mileage_std = np.std(mileage)

            mileage_normalized = normalize(mileage, mileage_mean, mileage_std)
            estimated_intercept, estimated_slope = training(mileage_normalized, price)
            intercept, slope = revert_normalize(estimated_intercept, estimated_slope, mileage_mean, mileage_std)
            regression_line = [intercept + slope * x for x in mileage]

            save_parameters(intercept, slope)
            visualize(mileage, price, regression_line)
        else:
            print("""
Usage:
    python training.py       # Train the model and display the regression line
    python training.py -d    # Display the data distribution only
        """)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
