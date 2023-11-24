from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SMAValue(Base):
    __tablename__ = 'sma_values'
    
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10))
    date = Column(Date)
    window_size = Column(Integer)
    sma = Column(Float)

    def __repr__(self):
        return f"<SMAValue(symbol={self.symbol}, date={self.date}, window_size={self.window_size}, sma={self.sma})>"
