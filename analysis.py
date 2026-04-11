import pandas as pd
import  matplotlib.pyplot as plt

# Load cleaned data (or original if same)
df = pd.read_csv("retail_sales_dataset.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# Create Total Sales column
df['Total_Sales'] = df['Quantity'] * df['Price per Unit']

# Extract Month
df['Month'] = df['Date'].dt.month

# -------------------------------
# 📈 1. Monthly Sales Trend
# -------------------------------
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("sales_trend.png")
plt.show()

# -------------------------------
# 📊 2. Sales by Product Category
# -------------------------------
category_sales = df.groupby('Product Category')['Total_Sales'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Product Category")
plt.savefig("category_sales.png")
plt.show()

# -------------------------------
# 👥 3. Sales by Gender
# -------------------------------
gender_sales = df.groupby('Gender')['Total_Sales'].sum()

plt.figure()
gender_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Gender")
plt.savefig("gender_sales.png")
plt.show()

print("✅ Analysis Completed")