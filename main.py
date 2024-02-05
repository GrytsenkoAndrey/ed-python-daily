import pandas as pd

df = pd.read_csv('salaries.csv')

#x = df.iloc[0, 1]
x = df.iloc[:3, :2]
#print(x)

#y = df.iloc[:, -1]
y = df.iloc[:, -1].values
# print(y)
print(y[0:5])