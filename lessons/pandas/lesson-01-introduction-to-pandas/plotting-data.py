import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame
df = pd.read_csv('data.csv')

# Plotting a histogram
df['Age'].plot(kind='hist')
plt.show()

# Plotting a bar chart
df.plot(kind='bar', x='Name', y='Salary')
plt.show()