from dotenv import load_dotenv
import requests
import os

url = "https://data.alpaca.markets/v2/stocks/RDBX/bars?start=2022-04-21T04:00:00-05:00&end=2022-04-21T09:00:00-05:00&timeframe=1Min"

load_dotenv()  # take environment variables from .env.
API_KEY = os.getenv("APCA-API-KEY-ID")
SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")
BASE_URL = os.getenv("APCA-API-BASE-URL")

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY
}
response = requests.get(url, headers=headers)

print(response.text)