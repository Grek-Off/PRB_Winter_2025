import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "avocado.csv"
df = pd.read_csv(file_path)

df = df.drop_duplicates()

types = df["type"].unique()
regions = df["region"].unique()

plt.boxplot(df["AveragePrice"])
plt.show()

