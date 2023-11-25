from flask import Flask, jsonify
import os
import requests

# Import blueprints
from performance.performance_blueprint import performance_bp
from strategy.strategy_blueprint import strategy_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(performance_bp, url_prefix='/api/performance')
app.register_blueprint(strategy_blueprint, url_prefix='/strategy')

@app.route('/test-alpaca-api', methods=['GET'])
def test_alpaca_api():
    # Your existing Alpaca API script
    # Ensure your API key and secret are properly set in environment variables
    url = "https://data.alpaca.markets/v2/stocks/RDBX/bars?..."
    API_KEY = os.getenv("APCA-API-KEY-ID")
    SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": SECRET_KEY
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json())  # Return the JSON response

# Rest of your Flask app code...
