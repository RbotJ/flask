from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'
    
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10), nullable=False)
    open_price = Column(Float)
    close_price = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Integer)
    date = Column(DateTime)

    def __repr__(self):
        return f"<StockData(symbol={self.symbol}, date={self.date}, open={self.open_price}, close={self.close_price})>"

# Replace 'your_mysql_connection_string' with your actual connection string
engine = create_engine('your_mysql_connection_string')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
