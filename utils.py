import pandas as pd
import json


def read_file():
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
    except Exception as e:
        print(f"Error: {e}")
        exit()
    return parameters["theta0"], parameters["theta1"]


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
