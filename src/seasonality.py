from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt

def decompose_product_category(df, category='Accessories', save_path='outputs/stl_result.png'):
    """
    Performs STL decomposition on monthly sales of a product category.
    """
    ts = df[df['Product_Category'] == category] \
        .groupby(df['Date'].dt.to_period('M'))['Order_Quantity'] \
        .sum().dropna()
    ts.index = ts.index.to_timestamp()

    if len(ts) < 24:
        print(f"[!] Not enough data points to decompose {category}. Skipped.")
        return

    stl = STL(ts, period=12)
    result = stl.fit()

    result.plot()
    plt.suptitle(f"STL Decomposition: {category}", fontsize=14)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[✔] STL decomposition saved at {save_path}")
