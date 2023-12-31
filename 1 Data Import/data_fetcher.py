import requests
from datetime import datetime, timedelta
from .models import StockData, Session

ALPACA_API_KEY = 'your_api_key'
ALPACA_API_SECRET = 'your_api_secret'
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'
HEADERS = {'APCA-API-KEY-ID': ALPACA_API_KEY, 'APCA-API-SECRET-KEY': ALPACA_API_SECRET}

def fetch_stock_data(symbol, start_date, end_date):
    session = Session()
    url = f"{ALPACA_BASE_URL}/v2/stocks/{symbol}/bars"
    params = {
        'start': start_date.isoformat(),
        'end': end_date.isoformat(),
        'timeframe': '1Day'
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code != 200:
        print(f"Error fetching data: {response.text}")
        return

    for bar in response.json():
        stock_data = StockData(
            symbol=symbol,
            open_price=bar['o'],
            close_price=bar['c'],
            high=bar['h'],
            low=bar['l'],
            volume=bar['v'],
            date=datetime.fromisoformat(bar['t'])
        )
        session.add(stock_data)
    session.commit()
    session.close()

def main():
    # Example usage
    yesterday = datetime.now() - timedelta(days=1)
    fetch_stock_data('TSLA', yesterday, datetime.now())

if __name__ == "__main__":
    main()
