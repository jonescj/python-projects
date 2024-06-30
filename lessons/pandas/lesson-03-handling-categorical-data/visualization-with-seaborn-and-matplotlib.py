import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset('tips')

# Create a box plot
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()

# Create a scatter plot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()
