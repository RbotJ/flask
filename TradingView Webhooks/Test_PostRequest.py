import requests

# Replace with your Flask app's webhook URL
webhook_url = 'http://localhost:5000/tradingview-webhook'

# Example payload similar to what TradingView would send
payload = {
    "ticker": "TSLA",
    "strategy.order.action": "buy",
    "strategy.order.price": 650.00,
    "strategy.order.contracts": 2
}

response = requests.post(webhook_url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
