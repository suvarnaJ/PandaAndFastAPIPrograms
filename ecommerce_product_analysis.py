import os
import pandas as pd

# E-Commerce Product Data Analysis
df = pd.read_csv("products.csv")

print("\nFIRST 5 RECORDS\n", df.head())
print("\nLAST 5 RECORDS\n", df.tail())
print("\nSHAPE:", df.shape)
print("\nCOLUMNS:", df.columns.tolist())
print("\nDATA TYPES\n", df.dtypes)
print("\nDATASET INFO")
df.info()
print("\nSTATISTICAL SUMMARY\n", df.describe())

print("\nTOTAL PRODUCTS:", len(df))
print("\nUNIQUE CATEGORIES:", df["category"].unique())
print("\nUNIQUE BRANDS:", df["brand"].unique())
print("\nCATEGORY-WISE COUNT\n", df["category"].value_counts())
print("\nAVERAGE PRICE:", df["price"].mean())

print("\nHIGHEST-PRICED PRODUCT\n", df.loc[df["price"].idxmax()])
print("\nLOWEST-PRICED PRODUCT\n", df.loc[df["price"].idxmin()])

print("\nPRODUCTS ABOVE ₹50,000\n", df[df["price"] > 50000])
print("\nPRODUCTS WITH RATING > 4\n", df[df["rating"] > 4])

print("\nSORTED BY PRICE\n", df.sort_values("price", ascending=False))
print("\nSORTED BY RATING\n", df.sort_values("rating", ascending=False))
print("\nSTOCK BELOW 10\n", df[df["stock"] < 10])

df["discount_amount"] = (df["price"] * df["discount"] / 100).round(2)
df["final_price"] = (df["price"] - df["discount_amount"]).round(2)

print("\nAVERAGE PRICE BY CATEGORY\n", df.groupby("category")["price"].mean().round(2))
print("\nAVERAGE RATING BY BRAND\n", df.groupby("brand")["rating"].mean().round(2))
print("\nMAXIMUM PRICE CATEGORY-WISE\n", df.groupby("category")["price"].max())

os.makedirs("output", exist_ok=True)
df.to_csv("output/final_product_data.csv", index=False)
print("\nFinal data exported successfully.")
