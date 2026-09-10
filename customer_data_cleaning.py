import pandas as pd

df = pd.read_csv("dirty_customer_data.csv")

print("DIRTY DATASET")
print(df.head(10))
print("Shape BEFORE:", df.shape)

print("\nMissing data using isnull():")
print(df.isnull())

print("\nMissing count using isnull().sum():")
print(df.isnull().sum())

print("\nDemonstrating dropna():")
print("Rows after dropna():", df.dropna().shape[0])

# Empty fields -> missing values
df = df.replace(r"^\\s*$", pd.NA, regex=True)

# Fill missing values
df["name"] = df["name"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")
df["email"] = df["email"].fillna("unknown@example.com")

# Convert numeric data
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["purchase_amount"] = pd.to_numeric(
    df["purchase_amount"].astype("string")
      .str.replace("Rs.", "", regex=False)
      .str.strip(),
    errors="coerce"
)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df["age"] = df["age"].fillna(df["age"].median())
df["purchase_amount"] = df["purchase_amount"].fillna(df["purchase_amount"].median())
df["rating"] = df["rating"].fillna(df["rating"].median())

print("\nDuplicate count using duplicated():", df.duplicated().sum())
print("\nDuplicate rows:")
print(df[df.duplicated(keep=False)])

df = df.drop_duplicates()

# Clean names and cities
df["name"] = df["name"].astype("string").str.strip().str.lower().str.title()
df["city"] = df["city"].astype("string").str.strip().str.lower().str.title()

# Demonstrate replace()
df["city"] = df["city"].replace({
    "Bombay": "Mumbai",
    "Bengaluru": "Bangalore"
})

# Correct data types
df["customer_id"] = df["customer_id"].astype("string")
df["age"] = df["age"].astype("int64")
df["purchase_amount"] = df["purchase_amount"].astype("float64")
df["rating"] = df["rating"].astype("float64")

print("\nCLEAN DATASET")
print(df.head(10))
print("Shape AFTER:", df.shape)
print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())
print("\nDuplicates AFTER cleaning:", df.duplicated().sum())

df.to_csv("cleaned_customer_data.csv", index=False)
print("\nSaved: cleaned_customer_data.csv")
