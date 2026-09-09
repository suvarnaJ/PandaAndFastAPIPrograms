import pandas as pd
import os

# =========================================================
# Sales Data Analysis
# =========================================================

# 1. Create/write the raw text file
sales_data = """order_id,product,quantity,price,city
101,Laptop,1,65000,Bangalore
102,Mouse,2,1200,Delhi
103,Keyboard,1,2500,Mumbai
104,Monitor,2,15000,Pune
105,Headphones,3,3000,Hyderabad
106,Laptop,1,72000,Chennai
107,Mouse,4,1000,Bangalore
108,Keyboard,2,2200,Delhi
109,Monitor,1,18000,Mumbai
110,Tablet,2,25000,Pune
111,Headphones,1,4500,Chennai
112,Laptop,2,58000,Hyderabad
113,Mouse,5,900,Mumbai
114,Keyboard,1,3500,Pune
115,Monitor,2,12500,Bangalore
116,Tablet,1,32000,Delhi
117,Headphones,2,2800,Mumbai
118,Laptop,1,85000,Pune
119,Mouse,3,1100,Chennai
120,Keyboard,2,3000,Hyderabad
121,Monitor,1,22000,Delhi
122,Tablet,2,28000,Bangalore
123,Headphones,4,2500,Pune
124,Laptop,1,69000,Mumbai
125,Mouse,2,1300,Hyderabad
126,Keyboard,3,1800,Chennai
127,Monitor,1,16500,Pune
128,Tablet,1,36000,Mumbai
129,Headphones,2,3200,Bangalore
130,Laptop,2,62000,Delhi
"""

with open("sales.txt", "w", encoding="utf-8") as file:
    file.write(sales_data)

print("sales.txt created successfully.")

# 2. Read using normal Python file handling
print("\n--- Reading using normal Python file handling ---")
with open("sales.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# 3. Load the same data using Pandas
df = pd.read_csv("sales.txt")

# 4. Convert into DataFrame
print("\n--- DataFrame ---")
print(df)

print("\n--- DataFrame Information ---")
print(df.info())

# 5. Calculate revenue = quantity * price
df["revenue"] = df["quantity"] * df["price"]

print("\n--- DataFrame with Revenue ---")
print(df)

# 6. Find total revenue
total_revenue = df["revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# 7. Find average order value
average_order_value = df["revenue"].mean()
print("Average Order Value:", round(average_order_value, 2))

# 8. Find highest-value order
highest_order = df.loc[df["revenue"].idxmax()]
print("\n--- Highest-Value Order ---")
print(highest_order)

# 9. Find lowest-value order
lowest_order = df.loc[df["revenue"].idxmin()]
print("\n--- Lowest-Value Order ---")
print(lowest_order)

# 10. Find revenue product-wise
product_revenue = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print("\n--- Revenue Product-Wise ---")
print(product_revenue)

# 11. Find revenue city-wise
city_revenue = df.groupby("city")["revenue"].sum().sort_values(ascending=False)
print("\n--- Revenue City-Wise ---")
print(city_revenue)

# 12. Save processed data as sales_report.csv
output_file = "sales_report.csv"
df.to_csv(output_file, index=False)

print(f"\nProcessed sales data saved successfully to: {output_file}")
