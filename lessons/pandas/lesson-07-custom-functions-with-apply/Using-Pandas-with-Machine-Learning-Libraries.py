import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Creating a sample DataFrame
df = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': 2 * np.linspace(0, 10, 100) + np.random.randn(100)
})
print(df)

# Preparing data for machine learning
X = df[['x']]
y = df['y']
print(X)
print(y)

# Splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train, X_test, y_train, y_test)


# Training a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting and evaluating the model
y_pred = model.predict(X_test)
print(f'R^2 Score: {model.score(X_test, y_test)}')