import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv("Penguins Data.csv")

df = pd.read_csv("Penguins Data.csv")
data = df[
    ["Culmen Length (mm)", "Culmen Depth (mm)",
     "Flipper Length (mm)", "Body Mass (g)"]
].dropna()

plt.figure()
plt.scatter(data["Culmen Length (mm)"], data["Body Mass (g)"])
plt.title("Scatter Plot: Culmen Length vs Body Mass")
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

scatter_matrix(data, figsize=(10, 10))
plt.suptitle("Pair Plot of Penguin Features", y=1.02)
plt.show()

data_sorted = data.sort_values("Culmen Length (mm)")

plt.figure()
plt.fill_between(data_sorted["Culmen Length (mm)"],
                 data_sorted["Body Mass (g)"])
plt.title("Area Graph: Culmen Length vs Body Mass")
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()