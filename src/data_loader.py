import pandas as pd

def load_and_prepare(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Order_Quantity'] > 0]  # drop invalid rows
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    return df
