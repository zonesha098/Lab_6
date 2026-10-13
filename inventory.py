
import pandas as pd
import matplotlib.pyplot as plt

# Create a messy inventory dataset for 10 products
products = [
    "Cola", "Chips", "Milk", "Biscuits", "Juice",
    "Yogurt", "Cookies", "Water", "Cheese", "Soda"
]

categories = [
    " beverages ", "SNACKS", " Dairy ", "Snacks", "beverages",
    "DAIRY", " snacks ", "BEVERAGES", "Dairy", " beverages "
]

prices = [
    "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 1,800",
    "Rs. 300", "Rs. 150", "Rs. 50", "Rs. 550", "Rs. 900"
]

stock = [40, 120, 60, 100, 35, 70, 90, 200, 45, 55]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Category": categories,
    "Price": prices,
    "Stock": stock
})

# Clean category names
df["Category"] = df["Category"].str.strip().str.title()

# Convert prices from text to numeric values
df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Encode categories into numeric codes
df["Category_Code"] = df["Category"].astype("category").cat.codes

# Print the cleaned DataFrame
print("Cleaned Inventory Data:")
print(df.to_string(index=False))

# Calculate average price for each category
average_prices = df.groupby("Category")["Price"].mean()

# Calculate each category's share of total stock
category_stock = df.groupby("Category")["Stock"].sum()

# Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot of average price
average_prices.plot(kind="bar", ax=axes[0])
axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=30)

# Pie chart of stock distribution
axes[1].pie(
    category_stock,
    labels=category_stock.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1].set_title("Share of Total Stock by Category")

plt.tight_layout()

# Save both plots in one image
plt.savefig("inventory_plots.png", dpi=300, bbox_inches="tight")
print("\nSaved inventory_plots.png")

plt.show()