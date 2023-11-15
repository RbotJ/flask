from dotenv import load_dotenv
import requests
import os
from sqlalchemy import create_engine
from get_stock_data import TechnicalData  # import your SQLAlchemy model
import pandas as pd

# Load environment variables
load_dotenv()
API_KEY = os.getenv("APCA-API-KEY-ID")
SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")
BASE_URL = os.getenv("APCA-API-BASE-URL")
DATABASE_URL = os.getenv("DATABASE_URL")

# Database engine
engine = create_engine(DATABASE_URL)

# Ticker symbols of the stocks to monitor
tickers = ['AAPL', 'TSLA', 'DIS']  # Add the rest of your 'magnificent 7' stocks

# Function to fetch and store stock data
def fetch_and_store_stock_data(ticker):
    url = f"{BASE_URL}/v2/stocks/{ticker}/bars?start=2022-04-21T04:00:00-05:00&end=2022-04-21T09:00:00-05:00&timeframe=1Min"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": SECRET_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # Parse and insert data into the database
    for item in data['bars']:
        # Create a TechnicalData object (or whatever your model is named)
        technical_data = TechnicalData(
            stock_id=...,
            timestamp=item['t'],
            open_price=item['o'],
            high_price=item['h'],
            low_price=item['l'],
            close_price=item['c'],
            volume=item['v'],
            # ... other fields ...
        )
        # Insert into the database
        with engine.connect() as connection:
            connection.execute(
                TechnicalData.__table__.insert(),
                **technical_data.__dict__
            )

# Fetch and store data for each ticker
for ticker in tickers:
    fetch_and_store_stock_data(ticker)

def get_stock_data(stock_ticker):
    # Database connection string
    # Replace 'mysql+pymysql://<username>:<password>@<host>/<dbname>' with your actual connection string
    connection_string = 'mysql+pymysql://<username>:<password>@<host>/<dbname>'

    # Create a database engine
    engine = create_engine(connection_string)

    # SQL query to select data
    # Replace table_name with your actual table name and ensure column names match your schema
    query = f"""
    SELECT Date, Open, High, Low, Close
    FROM table_name
    WHERE Ticker = '{stock_ticker}'
    ORDER BY Date
    """

    # Execute query and return a DataFrame
    df = pd.read_sql(query, con=engine)
    
    return df