import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("your_database_name.db")  # replace with actual DB file
cursor = conn.cursor()

# Load data into DataFrames
customers = pd.read_sql_query("SELECT * FROM customers", conn)
sales = pd.read_sql_query("SELECT * FROM sales", conn)
items = pd.read_sql_query("SELECT * FROM items", conn)

# Merge tables
merged = (
    items.merge(sales, on="sale_id")
         .merge(customers, on="customer_id")
)

# Filter for age 18–35 and non-null quantities
filtered = merged[
    (merged["age"].between(18, 35)) & (merged["quantity"].notnull())
]

# Group and sum
result = (
    filtered.groupby(["customer_id", "age", "item"], as_index=False)["quantity"]
           .sum()
)

# Filter out zero quantity
result = result[result["quantity"] > 0]

# Rename columns to match format
result.columns = ["Customer", "Age", "Item", "Quantity"]

# Save to CSV with semicolon delimiter
result.to_csv("output.csv", sep=';', index=False)
