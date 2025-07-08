import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_sales(df, save_path="outputs/monthly_sales.png"):
    """
    Plots total monthly sales quantity for each product category.
    """
    monthly = df.groupby([df['Date'].dt.to_period('M'), 'Product_Category'])['Order_Quantity'] \
                .sum().unstack().fillna(0)
    monthly.index = monthly.index.to_timestamp()

    plt.figure(figsize=(14, 6))
    monthly.plot(marker='o', ax=plt.gca())
    plt.title("Monthly Sales by Product Category")
    plt.xlabel("Date")
    plt.ylabel("Units Sold")
    plt.grid(True)
    plt.tight_layout()
    plt.legend(title="Product Category", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(save_path)
    plt.close()
    print(f"[✔] Monthly sales chart saved at {save_path}")
