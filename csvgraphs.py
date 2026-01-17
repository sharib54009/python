import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.plot(df['column1'])
plt.title("line plot")
plt.show()

plt.bar(df.index, df['column'])
plt.title("box plot")
plt.show()

plt.hist(df['column'])
plt.title("histogram")
plt.show()

plt.boxplot(df['column'])
plt.title("box plot")
plt.show()