import plotly.express as px
import pandas as pd
from your_data_module import get_stock_data  # Replace with your actual data fetching module

def create_stock_graph(stock_ticker):
    # Fetch stock data from your database
    df = get_stock_data(stock_ticker)  # This function should return a DataFrame with columns like 'Date', 'Open', 'High', 'Low', 'Close'

    # Create a candlestick chart using Plotly
    fig = px.line(df, x='Date', y='Close', title=f'Stock Price for {stock_ticker}')

    # Convert the figure to HTML
    graph_html = fig.to_html(full_html=False)

    return graph_html
