import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

# Load your CSV data with the correct date format
df = pd.read_csv('water_consumption_2015_2023.csv', delimiter=';', parse_dates=['Datum'], index_col='Datum', dayfirst=True)

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

# Plot the time series data
df['Wasserverbrauch'].plot(figsize=(10, 6))
plt.title('Water Consumption in Zurich')
plt.xlabel('Date')
plt.ylabel('Water Consumption')
plt.show()

# Perform the Augmented Dickey-Fuller test
result = adfuller(df['Wasserverbrauch'].dropna())
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')

# Fit ARIMA model
model = ARIMA(df['Wasserverbrauch'], order=(5, 1, 0))  # (p, d, q) parameters
model_fit = model.fit()

# Print the model summary
print(model_fit.summary())

# Ensure proper date index for forecasting
df_cleaned = df.asfreq('D')  # Ensure daily frequency

# Forecast the next 30 days
forecast = model_fit.forecast(steps=365)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Wasserverbrauch'], label='Historical Data')
plt.plot(pd.date_range(df.index[-1], periods=365, freq='D'), forecast, label='Forecast', color='red')
plt.title('Water Consumption Forecast for Zurich')
plt.xlabel('Date')
plt.ylabel('Water Consumption')
plt.legend()
plt.show()
