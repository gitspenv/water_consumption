import pandas as pd
import math
import matplotlib.pyplot as plt

def plot_aggregated_data(df, days=7, column='Wasserverbrauch'):

    # Ensure index is datetime (in case it's not already set)
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index, dayfirst=True)
    
    # Resample data by summing up over the specified number of days
    aggregated_data = df[column].resample(f'{days}D').sum()
    
    # Plot the aggregated data
    plt.figure(figsize=(10, 6))
    plt.plot(aggregated_data.index, aggregated_data.values, marker='o', label=f'{days}-Day Aggregated {column}')
    plt.title(f'{column} Aggregated Over {days}-Day Periods')
    plt.xlabel('Date')
    plt.ylabel(f'{column} (Aggregated)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_data(df, headers):
    """
    Plots data for the given headers from the DataFrame. The layout will adjust automatically
    based on the number of headers.

    Args:
    df (pd.DataFrame): The dataframe containing the data.
    headers (list): List of column names to plot.

    Returns:
    None
    """
    # Calculate the number of subplots needed
    num_plots = len(headers)
    num_cols = 2  # Number of columns in the subplot grid (you can adjust this as needed)
    num_rows = math.ceil(num_plots / num_cols)  # Number of rows needed
    
    # Create a figure with the calculated number of subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 6 * num_rows))

    # Flatten axes array in case of multiple rows/columns
    axes = axes.flatten()

    # List of colors to cycle through (expandable as needed)
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'cyan', 'black', 'yellow']

    for i, header in enumerate(headers):
        # Plot each data column on the respective axis
        axes[i].plot(df[header], label=header, color=colors[i % len(colors)])  # Cycle through colors
        axes[i].set_title(header)  # Title set to the header name
        axes[i].legend()
        axes[i].grid(True)

    # Turn off any unused subplots
    for i in range(num_plots, len(axes)):
        axes[i].axis('off')

    # Adjust layout for better appearance
    plt.tight_layout()
    plt.show()
