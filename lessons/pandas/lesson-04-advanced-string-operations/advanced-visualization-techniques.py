import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
iris = sns.load_dataset('iris')

# Create pair plot
sns.pairplot(iris)
plt.show()

# Create a heatmap
sns.heatmap(iris.corr(), annot=True, cmap='coolwarm')
plt.show()