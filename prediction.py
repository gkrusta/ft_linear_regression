from utils import load_parameters


def predict_price(mileage, intercept, slope):
    """
    Predict the price based on the mileage input using the regression model.
    """
    return (mileage * slope + intercept)


def main():
    try:
        intercept, slope = load_parameters()
        mileage = int(input("Enter mileage (in km): "))
        if mileage < 0:
            print("Error: Mileage has to be a positive int")
            exit()
        predicted_price = predict_price(mileage, intercept, slope)
        if predicted_price < 0:
            predicted_price = 0
        print(f"Predicted price is {int(predicted_price)} currency units.")
    except ValueError as ve: #throw another error for input if it's char, float etc...
        print(f"Error: Mileage has to be an int")
    except Exception as e: #throw another error for input if it's char, float etc...
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
