# 02_feature_engineering.ipynb

import pandas as pd
import numpy as np

# Load processed data
data = pd.read_csv('../data/processed/processed_data.csv')

# Feature engineering steps
# 1. Power Efficiency Ratio (Power/RPM)
data['Power_Efficiency_Ratio'] = data['Power'] / data['Rotational speed [rpm]']

# 2. Temperature-Torque Interaction
data['Temp_Torque_Interaction'] = data['Temp_Difference_°C'] * data['Torque [Nm]']

# 3. High Tool Wear Flag
threshold = 150  # as defined in the project
data['High_Tool_Wear_Flag'] = np.where(data['Tool wear [min]'] > threshold, 'High Wear', 'Normal Wear')

# Save the data with new features
data.to_csv('../data/processed/data_with_features.csv', index=False)