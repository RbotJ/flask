from alpaca_trade_api.rest import REST, TimeFrame

def fetch_stock_data(api_key, api_secret, base_url, symbol, start_date, end_date):
    alpaca = REST(api_key, api_secret, base_url)
    bars = alpaca.get_bars(symbol, TimeFrame.Day, start_date, end_date).df
    return bars
