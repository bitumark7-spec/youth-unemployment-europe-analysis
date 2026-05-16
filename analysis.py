import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load datasets
unemployment = pd.read_csv("data/unemployment.csv", skiprows=4)
inflation = pd.read_csv("data/inflation.csv", skiprows=4)
gdp = pd.read_csv("data/gdp.csv", skiprows=4)

# Keep needed columns
unemployment = unemployment[['Country Name', '2024']]
inflation = inflation[['Country Name', '2024']]
gdp = gdp[['Country Name', '2024']]

# Rename columns
unemployment.columns = ['Country', 'Unemployment']
inflation.columns = ['Country', 'Inflation']
gdp.columns = ['Country', 'GDP_Growth']

# Merge datasets
df = pd.merge(unemployment, inflation, on='Country')
df = pd.merge(df, gdp, on='Country')

# Remove missing values
df = df.dropna()

# Features
X = df[['Inflation', 'GDP_Growth']]

# Target
y = df['Unemployment']

# Train model
model = LinearRegression()
model.fit(X, y)

# Print coefficients
print("Intercept:", model.intercept_)
print("Coefficients:")
print("Inflation:", model.coef_[0])
print("GDP Growth:", model.coef_[1])
