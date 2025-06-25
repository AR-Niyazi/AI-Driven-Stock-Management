from src.data_loader import load_data
from src.model import train_model
from src.visualizer import plot_trends

df = load_data("data/sales_data.csv")
train_model(df)
plot_trends(df)
