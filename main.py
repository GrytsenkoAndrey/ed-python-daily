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

from sklearn.model_selection import train_test_split
x_train, x_text, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print(x_train.shape)