# AI-Driven Stock Management – Lahn Inc.

This project helps Lahn Inc., a global online retailer, make smarter stocking decisions. With limited storage space, the company needs to know what to stock more of and when. We use past sales data to spot trends, predict what will sell next month, and uncover seasonal buying patterns.

---

## 📊 What This Project Does

- Cleans and organizes historical sales data
- Visualizes monthly trends across product categories
- Detects seasonal sales cycles using time-series decomposition
- Predicts next month’s sales for specific products using:
  - Linear Regression
  - Random Forest Regression

---

## 💡 Why It Matters

Better forecasting helps Lahn Inc. avoid running out of popular items and wasting space on products that won’t sell. This project helps the company:
- Plan stock ahead of time
- Reduce overstock and understock
- Make more confident, data-driven inventory decisions

---

## 🛠 How to Use It

1. **Put your data file** in the `/data/` folder  
   File: `sales_data.csv`

2. **Run the main script:**
   ```bash
   python main.py
