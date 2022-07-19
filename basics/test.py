import pandas as pd 
import plotly.express as px

# read our excel sheet and sets it as a variable 
df_gold_prices = pd.read_csv('basics/monthly_gold_prices.csv')

# sets a key of the table to a variable
dates = df_gold_prices['Date']
prices = df_gold_prices['Price']

# creates a new column for 'buy price'
df_gold_prices['buy_price'] = prices * .9
print(df_gold_prices['buy_price'].max())

# instantiating a new graph then showing it in the browswer
fig = px.line(df_gold_prices, x = dates, y = prices, title = 'Gold Prices Over Time')
fig.show()