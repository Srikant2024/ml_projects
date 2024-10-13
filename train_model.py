import pandas as pd

df = pd.read_csv("house_prices_csv\Housing.csv")  # Replace with your dataset path
print(df.head())  # View the first few rows
  # Summary statistics
print(df.head())  # View the first few rows
print(df.info())  # Check data types and missing values
print(df.describe())  # Summary statistics
print(df.shape)  # Number of rows and columns
df.isnull().sum()  # Find missing values
df.fillna(df.mean(), inplace=True)  # Fill missing numerical values with the mean
df.dropna(inplace=True)  # Drop rows with missing values (if appropriate)
