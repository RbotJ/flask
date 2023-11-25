# api/risk_management.py

from flask import Blueprint, request, jsonify
from models.models import RiskManagement
from app import db

risk_management_blueprint = Blueprint('risk_management', __name__)

@risk_management_blueprint.route('/risk_management', methods=['POST'])
def set_risk_parameters():
    data = request.json
    new_risk_management = RiskManagement(
        strategy_id=data['strategy_id'],
        stop_loss=data['stop_loss'],
        take_profit=data['take_profit'],
        position_size=data['position_size']
    )
    db.session.add(new_risk_management)
    db.session.commit()
    return jsonify({"message": "Risk parameters set successfully"}), 201

# Additional routes as needed
