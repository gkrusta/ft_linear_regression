import json


def load_parameters():
    """
    Load the trained parameters from a JSON file.
    """
    try:
        with open("parameters.txt", "r") as file:
            parameters = json.load(file)
    except Exception as e:
        print(f"Error: {e}")
    return parameters["theta0"], parameters["theta1"]


def predict_price(mileage, intercept, slope):
    """
    Predict the price based on the mileage input using the regression model.
    """
    return (mileage * slope + intercept)


def main():
    try:
        intercept, slope = load_parameters()
        mileage = float(input("Enter mileage (in km): "))
        predicted_price = predict_price(mileage, intercept, slope)
        print(f"Predicted price is {predicted_price:.2f} currency units.")
    except Exception as e: #throw another error for input if it's char, float etc...
        print(f"Error: {e}")


if __name__ == "__main__":
    main()