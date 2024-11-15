import pandas as pd
import matplotlib.pyplot as plt


def plot_aggregated_data(df, days=7, column='Wasserverbrauch'):

    # Ensure index is datetime (in case it's not already set)
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index, dayfirst=True)
    
    # If days = 1, plot the original data without aggregation
    if days == 1:
        aggregated_data = df[column]
    else:
        # Resample data by summing up over the specified number of days
        aggregated_data = df[column].resample(f'{days}D').sum()
    
    # Plot the aggregated data
    plt.figure(figsize=(10, 6))
    plt.plot(aggregated_data.index, aggregated_data.values, marker='o', label=f'{days}-Day Aggregated {column}' if days > 1 else f'{column} (Original Data)')
    plt.title(f'{column} Aggregated Over {days}-Day Periods' if days > 1 else f'{column} (Original Data)')
    plt.xlabel('Date')
    plt.ylabel(f'{column} (Aggregated)' if days > 1 else f'{column}')
    plt.legend()
    plt.grid(True)
    plt.show()