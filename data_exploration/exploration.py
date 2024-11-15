import matplotlib.pyplot as plt
import load_clean_data as ld
import plot_functions as pl
import seaborn as sns

# Visualize data in basic plot
pl.plot_aggregated_data(ld.df, days=30, column='Wasserverbrauch')

# Show moving average
ld.df['rolling_mean'] = ld.df['Wasserverbrauch'].rolling(window=30).mean()
plt.plot(ld.df.index, ld.df['Wasserverbrauch'], label='Original')
plt.plot(ld.df.index, ld.df['rolling_mean'], label='30-Day Rolling Mean', color='red')
plt.legend()
plt.show()

# Check correlation --> which variable to keep/eliminate
sns.heatmap(ld.df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.show()


