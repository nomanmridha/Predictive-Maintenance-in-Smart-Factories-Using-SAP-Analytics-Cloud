# 01_data_preprocessing.ipynb

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load raw data
raw_data = pd.read_csv('../data/raw/predictive_maintenance.csv')

# Data inspection
print(raw_data.head())
print(raw_data.info())
print(raw_data.describe())

# Check for missing values
print(raw_data.isnull().sum())

# Handle missing values (if any)
# ...

# Remove duplicates
raw_data = raw_data.drop_duplicates()

# Convert data types if necessary
# ...

# Save processed data
raw_data.to_csv('../data/processed/processed_data.csv', index=False)