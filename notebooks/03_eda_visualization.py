# 03_eda_visualization.ipynb

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data with features
data = pd.read_csv('../data/processed/data_with_features.csv')

# Basic statistics
print(data.describe())

# Distribution of key variables
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
columns = ['Air_temp_°C', 'Process_temp_°C', 'Rotational speed [rpm]', 'Torque [Nm]', 'Power', 'Tool wear [min]']
for i, col in enumerate(columns):
    ax = axes[i//3, i%3]
    data[col].hist(ax=ax)
    ax.set_title(col)
plt.tight_layout()
plt.show()

# Correlation matrix
corr = data.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# More visualizations as needed