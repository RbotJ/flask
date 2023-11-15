#To use this script, add it to your Flask app, and run the create_schema() function when 
#initializing your app. Make sure SQLAlchemy is installed in your environment, and the 
#DATABASE_URL environment variable is set correctly in Railway. This will create the 
#necessary tables in your MySQL database upon deployment
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

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

class Fundamental(Base):
    __tablename__ = 'fundamentals'
    fundamental_id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stocks.stock_id'))
    fiscal_date_ending = Column(DateTime)
    reported_currency = Column(String(10))
    total_revenue = Column(Float)
    net_income = Column(Float)
    EPS = Column(Float)
    dividend_per_share = Column(Float)
    PE_ratio = Column(Float)
    ROE = Column(Float)
    debt_to_equity = Column(Float)
    free_cash_flow = Column(Float)
    stock = relationship("Stock")

class TechnicalData(Base):
    __tablename__ = 'technical_data'
    data_id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stocks.stock_id'))
    timestamp = Column(DateTime)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Integer)
    adjusted_close = Column(Float)
    granularity = Column(String(20))
    stock = relationship("Stock")

class AnalystAssessment(Base):
    __tablename__ = 'analyst_assessments'
    assessment_id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stocks.stock_id'))
    analyst_id = Column(Integer)
    date_of_assessment = Column(DateTime)
    resistance_levels = Column(String(500))
    support_levels = Column(String(500))
    predicted_movement = Column(String(500))
    assessment_notes = Column(String(1000))
    stock = relationship("Stock")

class Backtesting(Base):
    __tablename__ = 'backtesting'
    backtest_id = Column(Integer, primary_key=True)
    assessment_id = Column(Integer, ForeignKey('analyst_assessments.assessment_id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    performance_metric = Column(String(500))
    notes = Column(String(1000))
    assessment = relationship("AnalystAssessment")

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(100))
    role = Column(String(50))
    password_hash = Column(String(200))

def create_schema():
    database_url = os.environ.get("DATABASE_URL")
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
