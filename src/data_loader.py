import pandas as pd

def load_and_prepare(filepath):
    """
       Loads the sales dataset, cleans it, and adds useful time columns.
       - Converts 'Date' to datetime format
       - Removes rows with 0 sales
       - Extracts Month, Year, and Month-Year from the date
       """

    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])

    # Remove rows with zero or negative sales
    df = df[df['Order_Quantity'] > 0] # drop invalid rows

    # Add time features for grouping and analysis
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    return df
