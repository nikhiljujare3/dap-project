import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Data
data_url = r'D:\b.e\placement\project\cleaned.csv'  # Use raw string for path
data = pd.read_csv(data_url)

# Step 2: Data Exploration
print("Data Overview:")
print(data.head())
print("\nData Description:")
print(data.describe())
print("\nMissing Values:")
print(data.isnull().sum())

# Step 3: Data Visualization
# Distribution of Ratings
plt.figure(figsize=(10, 6))
sns.histplot(data['rating'], bins=5, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Average Amount Spent by Category
avg_amount_by_category = data.groupby('category')['amount'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
avg_amount_by_category.plot(kind='bar', color='skyblue')
plt.title('Average Amount Spent by Category')
plt.xlabel('Category')
plt.ylabel('Average Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 4: Sales Trends Over Time
# Create 'date' from year and month columns
data['date'] = pd.to_datetime(data[['year', 'month']].assign(day=1))

# Group by month and sum the 'amount'
monthly_sales = data.groupby(data['date'].dt.to_period('M'))['amount'].sum()

# Plotting the results
plt.figure(figsize=(14, 7))
monthly_sales.plot()
plt.title('Monthly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.grid()
plt.show()

# Step 5: Top Selling Products
top_selling_products = data.groupby('item_id')['quantity'].sum().nlargest(10)
top_selling_products.plot(kind='bar', color='lightgreen', figsize=(10, 6))
plt.title('Top Selling Products by Quantity')
plt.xlabel('Item ID')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 6: Save Processed Data
data.to_csv('processed_cleaned_data.csv', index=False)

# Optional: Save Visualizations
plt.savefig('monthly_sales.png')
