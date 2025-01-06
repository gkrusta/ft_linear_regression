# ft_linear_regression
A program that using machine learning algorithm can predict a price of a car based on it's mileage.

Why normalization is needed:
- Without normalization, features with large values (mileage) dominate features with smaller values (price).
- Gradient descent may take longer to converge or might not converge at all because the cost function’s shape becomes highly skewed.
