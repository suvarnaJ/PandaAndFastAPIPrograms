import os
import pandas as pd

# ---------------------------------------------------------
# Student Data Analysis using Pandas
# ---------------------------------------------------------

# 1. Read the CSV file
df = pd.read_csv("students.csv")

# 2. Display first 5 records
print("\n--- First 5 Records ---")
print(df.head())

# 3. Display last 5 records
print("\n--- Last 5 Records ---")
print(df.tail())

# 4. Display dataset shape
print("\n--- Dataset Shape ---")
print(df.shape)

# 5. Display all column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# 6. Display data types
print("\n--- Data Types ---")
print(df.dtypes)

# 7. Use info()
print("\n--- Dataset Info ---")
df.info()

# 8. Use describe()
print("\n--- Statistical Description ---")
print(df.describe())

# 9. Find average Python marks
print("\n--- Average Python Marks ---")
print(df["python_marks"].mean())

# 10. Find average SQL marks
print("\n--- Average SQL Marks ---")
print(df["sql_marks"].mean())

# 11. Find average Pandas marks
print("\n--- Average Pandas Marks ---")
print(df["pandas_marks"].mean())

# 12. Find maximum marks
marks_columns = ["python_marks", "sql_marks", "pandas_marks"]

print("\n--- Maximum Marks ---")
print(df[marks_columns].max())

# 13. Find minimum marks
print("\n--- Minimum Marks ---")
print(df[marks_columns].min())

# 14. Sort students by Python marks
print("\n--- Students Sorted by Python Marks ---")
print(df.sort_values(by="python_marks", ascending=False))

# 15. Sort students by attendance
print("\n--- Students Sorted by Attendance ---")
print(df.sort_values(by="attendance", ascending=False))

# 16. Filter students having Python marks greater than 80
print("\n--- Python Marks Greater Than 80 ---")
print(df[df["python_marks"] > 80])

# 17. Filter students having attendance greater than 75
print("\n--- Attendance Greater Than 75 ---")
print(df[df["attendance"] > 75])

# 18. Select only name, python_marks, and pandas_marks
print("\n--- Selected Columns ---")
print(df[["name", "python_marks", "pandas_marks"]])

# 19. Add total_marks column
df["total_marks"] = (
    df["python_marks"]
    + df["sql_marks"]
    + df["pandas_marks"]
)

# 20. Add average_marks column
df["average_marks"] = df["total_marks"] / 3

print("\n--- Final Dataset with Total and Average Marks ---")
print(df)

# 21. Save processed dataset
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "student_results.csv")
df.to_csv(output_file, index=False)

print(f"\nProcessed dataset saved successfully to: {output_file}")