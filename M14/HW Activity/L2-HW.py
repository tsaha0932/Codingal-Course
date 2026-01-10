import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 32, np.nan, 45, 21, 38],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Phoenix'],
    'Score': [85.5, 72.1, 90.0, 65.8, 98.2, 77.4]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("-" * 30)

print("DataFrame Info:")
df.info() 
print("-" * 30)

mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True) 
print(f"DataFrame after filling missing 'Age' with mean ({mean_age:.2f}):")
print(df)
print("-" * 30)

df.sort_values(by='Score', ascending=False, inplace=True)
print("DataFrame sorted by 'Score' (descending):")
print(df)
print("-" * 30)

df.drop(columns=['Passed'], inplace=True)
print("DataFrame after dropping 'Passed' column:")
print(df)
print("-" * 30)
