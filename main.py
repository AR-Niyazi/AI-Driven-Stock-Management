# AI-Driven Stock Management Pipeline

from src.data_loader import load_and_prepare
from src.visualizer import plot_monthly_sales
from src.seasonality import decompose_product_category
from src.model import train_predict

#STEP 1: Load the cleaned and prepared sales data
df = load_and_prepare("data/sales_data.csv")
print(df.head())

#STEP 2: Visualize monthly product category trends
plot_monthly_sales(df)

#STEP 3: See seasonal patterns for one category (e.g., Accessories)
decompose_product_category(df, category='Accessories', save_path='outputs/stl_accessories.png')
decompose_product_category(df, category='Clothing', save_path='outputs/stl_clothing.png')

#STEP 4: Predict next month's sales for a specific
train_predict(df, product_name="Hitch Rack - 4-Bike")

