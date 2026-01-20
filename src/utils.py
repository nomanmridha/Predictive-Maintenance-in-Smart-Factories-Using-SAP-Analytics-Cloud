# utils.py

def save_data(df, filepath):
    df.to_csv(filepath, index=False)