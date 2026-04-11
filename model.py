import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("retail_sales_dataset.csv")

# Prepare data
df['Total_Sales'] = df['Quantity'] * df['Price per Unit']

# Features & Target
X = df[['Quantity']]
y = df['Total_Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Show result
print("Sample Predictions:")
print(predictions[:5])

print("✅ Model Training Completed")