# feature_engineering.py

import numpy as np

def add_power_efficiency_ratio(df, power_col, rpm_col):
    df['Power_Efficiency_Ratio'] = df[power_col] / df[rpm_col]
    return df

def add_temp_torque_interaction(df, temp_diff_col, torque_col):
    df['Temp_Torque_Interaction'] = df[temp_diff_col] * df[torque_col]
    return df

def add_high_tool_wear_flag(df, tool_wear_col, threshold=150):
    df['High_Tool_Wear_Flag'] = np.where(df[tool_wear_col] > threshold, 'High Wear', 'Normal Wear')
    return df