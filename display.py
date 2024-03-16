from datetime import datetime
import pandas as pd
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import streamlit as st
from bs4 import BeautifulSoup
import time 
import requests

# Define function to fetch data for NSE
def fetch_nse_data(stock_symbol):
    url = f"https://www.google.com/finance/quote/{stock_symbol}:NSE?hl=en"
    
    # Make a request to the website
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract price information
        class_price = "YMlKec fxKbKc"
        class_PE = "P6K39c"
        price_element = soup.find(class_=class_price)
        price = float(price_element.text.strip()[1:].replace(",", ""))
        st.write(f"Price: {price}")

        
# Define function to fetch data for Nasdaq
def fetch_nasdaq_data(stock_symbol):
    data = yf.Ticker(stock_symbol).history(period='1d')
    st.write(data[['Open', 'High', 'Low']])
    return data



def main():
    st.title("Stock Data Fetcher")

    # Dropdown to select exchange
    exchange = st.selectbox("Select Exchange", ["NSE", "Nasdaq"])

    # Input box for stock symbol
    if exchange == "NSE":
        st.text("Enter Stock Symbol (e.g., ADANIENT for Adani Enterprises)")
        stock_symbol = st.text_input("Stock Symbol")
    elif exchange == "Nasdaq":
        st.text("Enter Stock Symbol (e.g., AAPL for Apple)")
        stock_symbol = st.text_input("Stock Symbol")

    # Button to trigger data fetching
    if st.button("Fetch Data"):
        if exchange == "NSE":
            fetch_nse_data(stock_symbol)
            st.success("NSE data fetched successfully!")
        elif exchange == "Nasdaq":
            fetch_nasdaq_data(stock_symbol)
            st.success("Nasdaq data fetched successfully!")

if __name__ == "__main__":
    main()
