import pandas as pd

df = pd.read_csv("Penguins Data.csv")

print("Dataset Information:\n")
print(df.info())

print("\nNull values in each column:\n")
print(df.isnull().sum())