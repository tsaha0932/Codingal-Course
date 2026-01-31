import pandas as pd
import matplotlib.pyplot as plt

july_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "New Births": [12, 15, 11, 9, 9, 21, 19]
}

df_july = pd.DataFrame(july_data)

plt.plot(df_july["Day"], df_july["New Births"])
plt.title("Birth Rate in July")
plt.xlabel("Day")
plt.ylabel("Number of Births")
plt.show()

august_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "New Births": [17, 5, 2, 11, 1, 8, 29]
}

df_august = pd.DataFrame(august_data)

plt.plot(df_august["Day"], df_august["New Births"])
plt.title("Birth Rate in August")
plt.xlabel("Day")
plt.ylabel("Number of Births")
plt.show()

plt.plot(df_july["Day"], df_july["New Births"],
         marker='o', linestyle='--', linewidth=2, label="July", color='blue')

plt.plot(df_august["Day"], df_august["New Births"],
         marker='s', linestyle='-.', linewidth=2, label="August", color='green')

plt.title("Birth Rate Comparison: July vs August")
plt.xlabel("Day")
plt.ylabel("Number of Births")
plt.legend()
plt.show()

x = list(range(1, 11))
y = [6 * 2 + i + 1 for i in x]

plt.plot(x, y, marker='^', linestyle='-', linewidth=2, color='red')
plt.title("Line Chart of Equation y = 6*2 + x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
