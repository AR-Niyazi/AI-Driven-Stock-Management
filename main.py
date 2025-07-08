from src.data_loader import load_and_prepare

df = load_and_prepare("data/sales_data.csv")
print(df.head())
