from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base

class Strategy(Base):
    __tablename__ = 'strategies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    stock_symbol = Column(String)
    active = Column(Boolean)

class Signal(Base):
    __tablename__ = 'signals'
    id = Column(Integer, primary_key=True)
    strategy_id = Column(Integer)
    signal_type = Column(String)
    price = Column(Float)
    timestamp = Column(Float)
