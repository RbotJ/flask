from alpaca_trade_api.rest import REST, TimeFrame
from sqlalchemy.orm import sessionmaker
from your_project.database import engine  # Import your database engine

class MovingAverageCalculator:
    def __init__(self, api_key, api_secret, base_url):
        self.alpaca = REST(api_key, api_secret, base_url)
        self.session = sessionmaker(bind=engine)()

    def calculate_sma(self, symbol, window_size, start_date, end_date):
        bars = self.alpaca.get_bars(symbol, TimeFrame.Day, start_date, end_date).df
        sma = bars['close'].rolling(window=window_size).mean()
        return sma

    def store_sma(self, symbol, sma):
        # Assuming you have a table for storing indicators
        # You would create a model in models.py and use it here to store the SMA values
        # Example:
        # new_sma_record = SMA(symbol=symbol, values=sma.tolist())
        # self.session.add(new_sma_record)
        # self.session.commit()

        pass  # Replace with actual storing logic

# Example usage
if __name__ == '__main__':
    api_key = 'your_api_key'
    api_secret = 'your_api_secret'
    base_url = 'https://paper-api.alpaca.markets'  # Use the appropriate URL

    ma_calculator = MovingAverageCalculator(api_key, api_secret, base_url)
    sma = ma_calculator.calculate_sma('AAPL', 20, '2021-01-01', '2021-12-31')
    ma_calculator.store_sma('AAPL', sma)
