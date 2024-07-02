import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a sample DataFrame
df = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

# Customizing a plot
plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'], label='Sine Wave')
plt.title('Sine Wave Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

import plotly.express as px

# Creating a sample DataFrame
df = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

# Creating an interactive plot
fig = px.line(df, x='x', y='y', title='Interactive Sine Wave Plot')
fig.show()