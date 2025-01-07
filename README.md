# ft_linear_regression
## Overview

The project trains a linear regression model to predict car prices based on mileage using a dataset of mileage-price pairs. The dataset is stored in `data.csv`.

The project includes:
- **Training Program**: Trains the model and saves parameters for future use.
- **Prediction Program**: Predicts car prices for given mileage values.
- **Precision Evaluation Program**: Calculates the precision of the model by comparing predicted prices with actual prices.

---

Why normalization is needed:
- Without normalization, features with large values (mileage) dominate features with smaller values (price).
- Gradient descent may take longer to converge or might not converge at all because the cost function’s shape becomes highly skewed.

theta1
The slope (theta1) represents the change in price per km.
It is normal for theta1 (slope) to be a small value if the scale of the input feature (mileage) is much larger than the scale of the target variable.
For example, if theta1 = −0.021, it means:
For every 1 km increase, the price decreases by 0.021 currency units.
Over a larger range (e.g., 10,000 km), the effect becomes noticeable:
Price decrease = 10,000⋅(−0.021) = −210 currency units.

theta0
The intercept (theta0) represents the base price when mileage is 0.
For example, if theta0 = 8499.53, it is the price when the car is new.

```
code
```

## Options to execute 

**`training.py`**: Trains the regression model and plots the results in a graph.

**`training.py -d`**: Displays a graph of the distribution of the data (no training).

**`predict.py`**: Predicts car prices based on user-input mileage.

**`precision.py`**: Calculates and displays the precision of the regression model.


## **Setup**

### 1. Install Requirements
This project requires Python and the following libraries:
- `numpy`
- `pandas`
- `matplotlib`
