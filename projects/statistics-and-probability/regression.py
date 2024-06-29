import numpy as np
import statsmodels.api as sm

def simple_linear_regression(X, y):
    if X.ndim == 1:
        X = X.reshape(-1, 1)  # Ensure X is 2D for consistency
    else:
        raise ValueError("X should be a 1-dimensional array for Simple Linear Regression.")
    X = sm.add_constant(X)  # Adds a constant term to the predictor
    model = sm.OLS(y, X).fit()
    return model

# Example usage:
# X = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 5, 7, 11])
# model = simple_linear_regression(X, y)
# print(model.summary())


def multiple_regression(X, y):
    if X.ndim == 1:
        raise ValueError("X should be a 2-dimensional array for Multiple Regression.")
    X = sm.add_constant(X)  # Adds a constant term to the predictors
    model = sm.OLS(y, X).fit()
    return model

# Example usage:
# X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
# y = np.array([2, 3, 5, 7, 11])
# model = multiple_regression(X, y)
# print(model.summary())


def correlation_coefficients(X, y):
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    
    corr_matrix = np.corrcoef(np.column_stack((X, y)), rowvar=False)
    corr_coeffs = corr_matrix[-1, :-1]  # Extract correlation coefficients for y with each X
    return corr_coeffs

# Example usage:
# X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
# y = np.array([2, 3, 5, 7, 11])
# print(correlation_coefficients(X, y))

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def logistic_regression(X, y, test_size=0.2, random_state=42):
    """
    Perform Logistic Regression.
    
    Parameters:
    X (DataFrame or array-like): Features
    y (Series or array-like): Target
    test_size (float): Proportion of the dataset to include in the test split
    random_state (int): Random state for reproducibility
    
    Returns:
    dict: Dictionary containing model, accuracy, and predictions
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return {
        'model': model,
        'accuracy': accuracy,
        'predictions': y_pred
    }
