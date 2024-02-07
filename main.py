import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('salaries.csv')

x = df.iloc[:, :-1].values
y = df.iloc[:, :-1].values

plt.scatter(x, y)
plt.show()