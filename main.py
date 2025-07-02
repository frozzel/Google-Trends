import pandas as pd
import matplotlib.pyplot as plt

df_tesla = pd.read_csv('Data/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Data/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('Data/UE Benefits Search vs UE Rate 2004-19.csv')

print(df_tesla.shape)
print(df_tesla.head())

print(f'Largest value for Tesla in Web Search: ') 
print(f'Smallest value for Tesla in Web Search: ')

