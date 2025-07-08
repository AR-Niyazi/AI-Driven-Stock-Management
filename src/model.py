import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_predict(df, product_name="Hitch Rack - 4-Bike"):
    """

    Predict next month's sales for a given product using:
    - Linear Regression
    - Random Forest Regression

    We use the previous month's sales as a simple feature.

    """
    # Filter and group monthly sales for the product
    product_df = df[df['Product'] == product_name].copy()
    monthly = product_df.groupby(['Year', 'Month'])['Order_Quantity'].sum().reset_index()

    # Create a date and lag column
    monthly['Date'] = pd.to_datetime(monthly[['Year', 'Month']].assign(DAY=1))
    monthly['Lag_1'] = monthly['Order_Quantity'].shift(1)
    monthly = monthly.dropna()

    X = monthly[['Lag_1']]
    y = monthly['Order_Quantity']

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X, y)
    y_pred_lr = lr.predict(X)

    # Random Forest Regression
    rf = RandomForestRegressor()
    rf.fit(X, y)
    y_pred_rf = rf.predict(X)

    # Print results
    print(f"🔹 {product_name} Sales Forecasting Results")
    print("Linear Regression:")
    print(f"  RMSE: {mean_squared_error(y, y_pred_lr) ** 0.5:.2f}")
    print(f"  R²:   {r2_score(y, y_pred_lr):.2f}")

    print("Random Forest Regression:")
    print(f"  RMSE: {mean_squared_error(y, y_pred_rf) ** 0.5:.2f}")
    print(f"  R²:   {r2_score(y, y_pred_rf):.2f}")
