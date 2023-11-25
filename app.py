from flask import Flask, jsonify, render_template
import requests
import os
from flask import Flask
from performance.performance_blueprint import performance_bp

app = Flask(__name__)

# Register the performance blueprint
app.register_blueprint(performance_bp, url_prefix='/api/performance')


app = Flask(__name__)
from strategy.strategy_blueprint import strategy_blueprint

app.register_blueprint(strategy_blueprint, url_prefix='/strategy')
from flask import Flask
from performance.performance_api import performance_bp

app = Flask(__name__)
app.register_blueprint(performance_bp, url_prefix='/api')

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

# ... your existing Flask app code ...
