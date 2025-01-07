from utils import read_file, load_parameters


def get_precisioin(actual_p, predicted_p):
    """
    Calculate Mean Absolute Error (MAE) in percentage.
    """
    total_error = sum(abs((p - a) / a) for p, a in zip(predicted_p, actual_p))
    return total_error / len(actual_p) * 100


def main():
    mileage, actual_price = read_file()
    theta0, theta1 = load_parameters()
    predicted_price = [km * theta1 + theta0 for km in mileage]
    mae = get_precisioin(actual_price, predicted_price)
    print(f"Mean Absolute Error (MAE): {mae:.2f}%")


if __name__ == "__main__":
    main()
