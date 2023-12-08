from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/tradingview-webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook data received:", data)
    # Process the data (e.g., place trades, log data, etc.)
    return jsonify({"status": "success", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
