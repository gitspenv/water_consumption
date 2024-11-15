import pandas as pd

# Load your CSV data with the correct date format
df = pd.read_csv('./water_consumption_2015_2023.csv', delimiter=';', parse_dates=['Datum'], index_col='Datum', dayfirst=True)

# Display the first few rows to inspect the data
print(df.head())

# Calculate IQR and filter out outliers
Q1 = df['Wasserverbrauch'].quantile(0.25)  # First quartile (25th percentile)
Q3 = df['Wasserverbrauch'].quantile(0.75)  # Third quartile (75th percentile)
IQR = Q3 - Q1  # Interquartile Range

# Define outlier thresholds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
df = df[(df['Wasserverbrauch'] >= lower_bound) & (df['Wasserverbrauch'] <= upper_bound)]

# Convert all columns to numeric (float64), invalid values will be set as NaN
df = df.apply(pd.to_numeric, errors='coerce')

print(df.columns)