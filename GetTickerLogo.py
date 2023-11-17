from dotenv import load_dotenv
import os
import requests
load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
API_KEY = os.getenv("APCA-API-KEY-ID")
SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")
url = "https://data.alpaca.markets/v1beta1/logos/aapl?placeholder=true"

headers = {
    "accept": "image/png",
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY
}

response = requests.get(url, headers=headers)

print(response.text)