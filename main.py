import yfinance as yf
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Function to fetch historical stock data from Yahoo Finance
def get_historical_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# Function to train ARIMA model
def train_arima(data):
    # Taking 'Close' prices as our target variable
    close_prices = data['Close'].values
    
    # Fitting ARIMA model
    model = ARIMA(close_prices, order=(5,1,0)) # ARIMA(p,d,q) with p=5, d=1, q=0
    model_fit = model.fit()
    
    return model_fit

# Function to train SARIMA model
def train_sarima(data):
    # Taking 'Close' prices as our target variable
    close_prices = data['Close']
    
    # Fitting SARIMA model
    model = SARIMAX(close_prices, order=(5, 1, 0), seasonal_order=(1, 1, 1, 12))  # SARIMA(p,d,q)(P,D,Q)m with p=5, d=1, q=0, P=1, D=1, Q=1, m=12
    model_fit = model.fit()
    
    return model_fit

# Main function for ARIMA
def main_arima():
    # Fetching historical data
    symbol = 'TSLA'  # Example stock symbol (Tesla Inc.)
    start_date = '2022-01-01'
    end_date = '2024-03-16'
    data = get_historical_data(symbol, start_date, end_date)
    
    # Training ARIMA model
    arima_model = train_arima(data)
    
    # Generating ARIMA predictions
    arima_forecast = arima_model.forecast(steps=7)  # Forecasting next 5 steps
    
    print("ARIMA Forecast:")
    print(arima_forecast)

# Main function for SARIMA
def main_sarima():
    # Fetching historical data
    symbol = 'TSLA'  # Example stock symbol (Tesla Inc.)
    start_date = '2022-01-01'
    end_date = '2024-03-16'
    data = get_historical_data(symbol, start_date, end_date)
    
    # Training SARIMA model
    sarima_model = train_sarima(data)
    
    # Generating SARIMA predictions
    sarima_forecast = sarima_model.forecast(steps=5)  # Forecasting next 5 steps
    
    print("SARIMA Forecast:")
    print(sarima_forecast)

if __name__ == "__main__":
    main_arima()
    main_sarima()

