import pandas as pd
import numpy as np
import tensorflow as tf

# Creating a sample DataFrame
df = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': 2 * np.linspace(0, 10, 100) + np.random.randn(100)
})

# Preparing data for TensorFlow
X = df[['x']]
y = df['y']

# Creating TensorFlow dataset
dataset = tf.data.Dataset.from_tensor_slices((X.values, y.values))
for feature, target in dataset.take(5):
    print(f'Features: {feature}, Target: {target}')