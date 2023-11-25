from . import performance_bp
from .performance_calculator import calculate_performance
from flask import jsonify, request
from .models import TradePerformance
from app import db

@performance_bp.route('/calculate_performance', methods=['POST'])
def calculate_and_store_performance():
    data = request.json
    strategy_id = data.get('strategy_id')

    # Perform calculations (this could be more complex in reality)
    performance = calculate_performance(strategy_id)

    # Return the calculated performance metrics
    return jsonify({"strategy_id": strategy_id,
                    "total_return": performance.total_return,
                    "win_ratio": performance.win_ratio,
                    "drawdown": performance.drawdown})

@performance_bp.route('/performance/<int:strategy_id>', methods=['GET'])
def get_performance(strategy_id):
    performance = TradePerformance.query.filter_by(strategy_id=strategy_id).first()
    if performance:
        return jsonify({"total_return": performance.total_return,
                        "win_ratio": performance.win_ratio,
                        "drawdown": performance.drawdown})
    else:
        return jsonify({"error": "Performance data not found"}), 404
