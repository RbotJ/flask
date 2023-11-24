from alpaca_trade_api import REST
from models import Strategy, Signal
from sqlalchemy.orm import sessionmaker
from utils import calculate_indicator, check_strategy_conditions

class SignalGenerator:
    def __init__(self, alpaca_api: REST, db_session: sessionmaker):
        self.alpaca_api = alpaca_api
        self.db_session = db_session

    def generate_signals(self):
        strategies = self._get_active_strategies()
        for strategy in strategies:
            data = self._fetch_market_data(strategy.stock_symbol)
            signal = self._evaluate_strategy(data, strategy)
            if signal:
                self._store_signal(signal)

    def _get_active_strategies(self):
        session = self.db_session()
        strategies = session.query(Strategy).filter(Strategy.active == True).all()
        session.close()
        return strategies

    def _fetch_market_data(self, symbol):
        # Fetch market data from Alpaca
        pass

    def _evaluate_strategy(self, market_data, strategy):
        # Evaluate the given strategy against the market data
        pass

    def _store_signal(self, signal):
        session = self.db_session()
        session.add(signal)
        session.commit()
        session.close()
