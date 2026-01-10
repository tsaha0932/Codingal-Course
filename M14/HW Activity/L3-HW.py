import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def visualize_dataset_parameters(data):
    
    print("Starting data visualization...")

    plt.figure(figsize=(8, 6))
    plt.scatter(data['Feature1'], data['Feature2'], alpha=0.6, edgecolors='w', s=100)
    plt.title('Scatter Plot of Feature1 vs Feature2')
    plt.xlabel('Feature1 Value')
    plt.ylabel('Feature2 Value')
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.hist(data['Feature1'], bins=15, color='skyblue', edgecolor='black')
    plt.title('Histogram of Feature1 Distribution')
    plt.xlabel('Feature1 Value')
    plt.ylabel('Frequency')
    plt.show()

    category_counts = data['Category'].value_counts()
    plt.figure(figsize=(8, 6))
    category_counts.plot(kind='bar', color=['coral', 'lightgreen', 'gold'])
    plt.title('Bar Chart of Category Counts')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()
    
    print("Visualizations complete.")

