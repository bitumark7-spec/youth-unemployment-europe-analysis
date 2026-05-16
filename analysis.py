import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load datasets
unemployment = pd.read_csv("data/unemployment.csv", skiprows=4)
inflation = pd.read_csv("data/inflation.csv", skiprows=4)

# Keep needed columns
unemployment = unemployment[['Country Name', '2024']]
inflation = inflation[['Country Name', '2024']]

# Rename columns
unemployment.columns = ['Country', 'Unemployment']
inflation.columns = ['Country', 'Inflation']

# Merge datasets
df = pd.merge(unemployment, inflation, on='Country')

# Remove missing values
df = df.dropna()

# Correlation
correlation = df['Inflation'].corr(df['Unemployment'])

print("Correlation:", correlation)

# Regression model
X = df[['Inflation']]
y = df['Unemployment']

model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Scatter plot
plt.scatter(df['Inflation'], df['Unemployment'])

# Regression line
plt.plot(df['Inflation'], y_pred)

# Labels
plt.xlabel("Inflation Rate (%)")
plt.ylabel("Youth Unemployment Rate (%)")
plt.title("Inflation vs Youth Unemployment (2024)")

# Save graph
plt.savefig("images/inflation_vs_unemployment.png")

# Show graph
plt.show()
