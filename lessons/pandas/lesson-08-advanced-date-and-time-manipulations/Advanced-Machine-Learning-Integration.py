import pandas as pd

import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Creating a sample DataFrame
df = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': 2 * np.linspace(0, 10, 100) + np.random.randn(100)
})

# Preparing data for machine learning
X = df[['x']]
y = df['y']

# Splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training an XGBoost model
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Predicting and evaluating the model
y_pred = model.predict(X_test)
print(f'RMSE: {mean_squared_error(y_test, y_pred, squared=False)}')