import pandas as pd

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
iris = sns.load_dataset('iris')

# Create scatter matrix
scatter_matrix = pd.plotting.scatter_matrix(iris, figsize=(10, 10))
plt.show()

import plotly.express as px

# Create a sample DataFrame
df = pd.DataFrame({
    'x': range(10),
    'y': [x**2 for x in range(10)]
})

# Create an interactive line plot
fig = px.line(df, x='x', y='y', title='Interactive Line Plot')
fig.show()