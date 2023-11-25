from flask import Blueprint, jsonify
from .performance_calculator import calculate_performance

performance_bp = Blueprint('performance', __name__)

@performance_bp.route('/performance/<int:strategy_id>', methods=['GET'])
def get_performance(strategy_id):
    performance = calculate_performance(strategy_id)
    return jsonify({"total_return": performance.total_return,
                    "win_ratio": performance.win_ratio,
                    "drawdown": performance.drawdown})
