import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01') # download data for a specific stock
print(stock_data.head())
print(stock_data.isnull().sum()) # check for missing values
stock_data.fillna(stock_data.mean(), inplace=True) # fill missing values with the mean
stock_data['returns'] = stock_data['Close'].pct_change() # calculate daily returns
stock_data['returns'].hist(bins=50) # plot a histogram of daily returns
stock_data['returns'].plot(figsize=(10, 6)) # plot a line chart of daily returns
stock_data.dropna(inplace=True) # drop rows with missing values
print(stock_data.head())
  #cumulative returns
stock_data['cumulative_returns'] = (1 + stock_data['returns']).cumprod()
stock_data['50_ma'] = stock_data['Close'].rolling(window=50).mean()
stock_data['200_ma'] = stock_data['Close'].rolling(window=200).mean()
#print(stock_data[['Close','returns ','cumulative_returns','50_ma','200_ma']].head())
#plotting
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'],label='Close Price')
plt.plot(stock_data['50_ma'],label='50-day MA')
plt.plot(stock_data['200_ma'],label='200-day MA')
plt.title('Stock Price with Moving Averages')
plt.legend()
plt.show()
 # plot daily returns
plt.figure(figsize=(10, 6))
plt.plot(stock_data['returns'],label='Daily Returns')
plt.title('Stock Daily Returns')
plt.show()
#plot cumulative returns
plt.figure(figsize=(10, 6))
plt.plot(stock_data['cumulative_returns'],label='Cumulative Returns')
plt.title('Stock Cumulative Returns')
plt.legend()
plt.show()
#statistical analysis
volatility = stock_data['returns'].std()
print(f'Volatility: {volatility:.4f}')
tickers=['AAPL', 'GOOG', 'MSFT']
stock_data_multi = yf.download(tickers, start='2020-01-01', end='2023-01-01')
stock_returns = stock_data_multi.pct_change()
correlation_matrix = stock_returns.corr()
print(correlation_matrix)
plt.figure(figsize=(6, 4 ))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
#save
stock_data.to_csv('aapl_stock_analysis.csv')
plt.savefig('stock_price_plot.png')
