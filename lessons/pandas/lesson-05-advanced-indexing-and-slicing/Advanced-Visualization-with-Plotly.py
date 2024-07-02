import pandas as pd
import numpy as np
import plotly.express as px

# Create a random DataFrame
np.random.seed(42)
df = pd.DataFrame({
    'A': np.random.randn(100),  # 100 random numbers from a normal distribution
    'B': np.random.rand(100)    # 100 random numbers from a uniform distribution
})

# Create an interactive scatter plot
fig = px.scatter(df, x='A', y='B', title='Scatter plot of A vs B')
fig.show()

# Create an interactive histogram
fig = px.histogram(df, x='A', nbins=30, title='Histogram of A')
fig.show()