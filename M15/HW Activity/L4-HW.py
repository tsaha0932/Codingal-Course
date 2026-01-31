import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Penguins Data.csv")

plt.hist(df["Culmen Length (mm)"].dropna(),
         bins=10, color="blue")
plt.title("Histogram of Culmen Length (mm)")
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Frequency")
plt.show()

plt.hist(df["Culmen Depth (mm)"].dropna(),
         bins=10, color="green")
plt.title("Histogram of Culmen Depth (mm)")
plt.xlabel("Culmen Depth (mm)")
plt.ylabel("Frequency")
plt.show()

plt.hist(df["Flipper Length (mm)"].dropna(),
         bins=12, color="orange")
plt.title("Histogram of Flipper Length (mm)")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")
plt.show()

plt.hist(df["Body Mass (g)"].dropna(),
         bins=12, color="red")
plt.title("Histogram of Body Mass (g)")
plt.xlabel("Body Mass (g)")
plt.ylabel("Frequency")
plt.show()
