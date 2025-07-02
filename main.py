import pandas as pd
import matplotlib.pyplot as plt

df_tesla = pd.read_csv('Data/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Data/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('Data/UE Benefits Search vs UE Rate 2004-19.csv')

print(df_tesla.shape)
print(df_tesla.head())

print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}') 
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')

print(df_tesla.describe())

# increases size and resolution
plt.figure(figsize=(14,8), dpi=120) 
plt.title('Tesla Web Search vs Price', fontsize=18)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
 
# Displays chart explicitly
plt.show()
