import requests
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database and API configurations
database_url = os.getenv("Mysql_URL")
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
alpha_vantage_url = "https://www.alphavantage.co/query"

# SQLAlchemy setup
engine = create_engine(database_url)

# Stock Table Model (simplified for illustration)
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

Base = declarative_base()

class Stock(Base):
    __tablename__ = 'stocks'
    stock_id = Column(Integer, primary_key=True)
    ticker_symbol = Column(String(10), unique=True)
    company_name = Column(String(100))
    sector = Column(String(50))
    industry = Column(String(50))
    market_cap = Column(Float)
    IPO_date = Column(DateTime)
    # Add additional fields as needed

def get_stock_info(ticker):
    overview_params = {
        "function": "OVERVIEW",
        "symbol": ticker,
        "apikey": alpha_vantage_api_key
    }
    overview_response = requests.get(alpha_vantage_url, params=overview_params)

    if overview_response.status_code == 200 and 'Symbol' in overview_response.json():
        overview_data = overview_response.json()
        return overview_data
    else:
        return None

def add_stock_to_db(stock_info):
    try:
        new_stock = Stock(
            ticker_symbol=stock_info['Symbol'],
            company_name=stock_info.get('Name', 'N/A'),
            sector=stock_info.get('Sector', 'N/A'),
            industry=stock_info.get('Industry', 'N/A'),
            market_cap=float(stock_info.get('MarketCapitalization', 0)),
            IPO_date=stock_info.get('IPOyear')  # Handle date conversion as needed
            # Add additional fields here
        )
        with Session(engine) as session:
            session.add(new_stock)
            session.commit()
            # Move the print statement inside the session block
            print(f"Stock added to Watchlist: {new_stock.ticker_symbol}, {new_stock.company_name}")
    except SQLAlchemyError as e:
        print(f"Error adding stock to database: {e}")


def main():
    ticker = input("Enter the stock ticker you'd like to add: ")
    with Session(engine) as session:
        existing_stock = session.execute(select(Stock).where(Stock.ticker_symbol == ticker)).scalar()
        if existing_stock:
            print(f"{ticker} already exists in the database.")
            return

    stock_info = get_stock_info(ticker)
    if stock_info:
        add_stock_to_db(stock_info)
    else:
        print(f"{ticker} is not a valid stock ticker or no data available.")

if __name__ == "__main__":
    main()
