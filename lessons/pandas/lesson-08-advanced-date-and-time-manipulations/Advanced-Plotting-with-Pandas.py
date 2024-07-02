import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a sample DataFrame
df = pd.DataFrame({
    'x': np.random.randn(1000),
    'y': np.random.randn(1000)
})

# Creating a hexbin plot
df.plot.hexbin(x='x', y='y', gridsize=30)
plt.show()

from pandas.plotting import andrews_curves

# Load the iris dataset
iris = sns.load_dataset('iris')

# Plot Andrews curves
andrews_curves(iris, 'species')
plt.show()