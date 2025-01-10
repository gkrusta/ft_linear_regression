import pandas as pd
import json
import matplotlib.pyplot as plt


def visualize(mileage, price, regression_line=None):
    """
    Visualize the data distribution and optionally the regression line.
    """
    try:
        plt.figure(figsize = (14,10))
        plt.scatter(mileage, price, marker='o', color='red', label='Data points')
        if regression_line is not None:
            plt.plot(mileage, regression_line, color='blue', linestyle='dashed', label='Regression line')
        plt.xlabel("Mileage (in km)", fontsize=14, fontweight="bold", labelpad=20)
        plt.ylabel('price', fontsize=14, fontweight="bold", labelpad=20)
        plt.legend(loc="upper right", fontsize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.title("Car Price vs Mileage", fontsize=20, fontweight="bold", pad=20)
        plt.show()
        plt.close()
    except KeyboardInterrupt:
        print("\nVisualization interrupted by the user. Exiting cleanly.")
    except Exception as e:
        print(f"Error: {e}")


def read_file():
    """
    Open the .csv file and save the mileage and price in a list.
    """
    try:
        data = pd.read_csv("data.csv")
        mileage = data['km'].tolist()
        price = data['price'].tolist()
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        exit()
    except Exception as e:
        print(f"Error reading dataset: {e}")
        exit()
    return mileage, price


def load_parameters():
    """
    Load the trained parameters from a JSON file.
    """
    try:
        with open("parameters.txt", "r") as file:
            parameters = json.load(file)
        return parameters["theta0"], parameters["theta1"]
    except FileNotFoundError:
        print("Warning: Parameters file not found.")
        return 0, 0 
    except Exception as e:
        print(f"Error: {e}")
        exit()


def save_parameters(theta0, theta1):
    """
    Save the trained parameters to a JSON file.
    """
    parameters = {"theta0": theta0, "theta1": theta1}
    try:
        with open("parameters.txt", "w") as file:
            json.dump(parameters, file)
    except Exception as e:
        print(f"Error: {e}")
        exit()
