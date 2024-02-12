import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('salaries.csv')

# Split the data into x and y
x = df.iloc[:, :-1].values
y = df.iloc[:, :-1].values

# Plot the data
plt.scatter(x, y)
plt.show()
