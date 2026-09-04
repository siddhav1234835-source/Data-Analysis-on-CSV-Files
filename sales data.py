# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# 1.CREATE SALES DATA

data = {
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04",
        "2026-01-05",
        "2026-01-06",
        "2026-01-07",
        "2026-01-08",
        "2026-01-09",
        "2026-01-10"
    ],

    "Product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Chair",
        "Laptop",
        "Mouse",
        "Table",
        "Keyboard",
        "Chair",
        "Laptop"
    ],

    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Furniture",
        "Electronics",
        "Electronics",
        "Furniture",
        "Electronics",
        "Furniture",
        "Electronics"
    ],

    "Quantity": [
        45, 56, 34, 23, 19,
        80, 16, 41, 39, 72
    ],

    "Price": [
        50500, 6900, 15300, 8400, 93000,
        7800, 123300, 45400, 45600, 54000
    ]
}


# Create DataFrame
df = pd.DataFrame(data)

# 2.SAVE DATA AS CSV

df.to_csv("sales_data.csv", index=False)

print("CSV file created successfully!")
print()

# 3.LOAD CSV FILE

df = pd.read_csv("sales_data.csv")

print("      FIRST 5 ROWS       ")
print(df.head())
print()

# 4.BASIC DATA INFORMATION

print("      DATASET INFORMATION      ")
df.info()
print()


print("      DATASET SHAPE      ")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print()


print("      COLUMN NAMES     ")
print(df.columns.tolist())
print()

# 5.CHECK MISSING VALUES

print("      MISSING VALUES      ")
print(df.isnull().sum())
print()

# 6.CALCULATE SALES

df["Sales"] = df["Quantity"] * df["Price"]

print("     DATA WITH SALES      ")
print(df)
print()

# 7.TOTAL SALES

total_sales = df["Sales"].sum()

print("       TOTAL SALES      ")
print("Total Sales:", total_sales)
print()

# 8.TOTAL QUANTITY SOLD

total_quantity = df["Quantity"].sum()

print("      TOTAL QUANTITY SOLD      ")
print("Total Quantity Sold:", total_quantity)
print()

# 9.SALES BY PRODUCT

sales_by_product = df.groupby("Product")["Sales"].sum()

print("      SALES BY PRODUCT      ")
print(sales_by_product)
print()

# 10.QUANTITY BY PRODUCT

quantity_by_product = df.groupby("Product")["Quantity"].sum()

print("      QUANTITY BY PRODUCT      ")
print(quantity_by_product)
print()

# 11.SALES BY CATEGORY

sales_by_category = df.groupby("Category")["Sales"].sum()

print("      SALES BY CATEGORY      ")
print(sales_by_category)
print()

# 12.BEST SELLING PRODUCT

best_product = sales_by_product.idxmax()
highest_sales = sales_by_product.max()

print("      BEST SELLING PRODUCT     ")
print("Best Selling Product:", best_product)
print("Highest Product Sales:", highest_sales)
print()

# 13.CHART 1 - SALES BY PRODUCT

plt.figure(figsize=(8, 5))

sales_by_product.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(axis="y")

plt.tight_layout()
plt.show()

# 14.CHART 2 - SALES BY CATEGORY

plt.figure(figsize=(7, 5))

sales_by_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.grid(axis="y")

plt.tight_layout()
plt.show()

# 15.CHART 3 - QUANTITY SOLD

plt.figure(figsize=(8, 5))

quantity_by_product.plot(kind="bar")

plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.grid(axis="y")

plt.tight_layout()
plt.show()

# 16.FINAL SUMMARY

print("      FINAL SALES SUMMARY     ")

print("Total Sales:", total_sales)
print("Total Quantity Sold:", total_quantity)
print("Best Selling Product:", best_product)
print("Highest Product Sales:", highest_sales)

print("      ANALYSIS COMPLETED SUCCESSFULLY      ")
