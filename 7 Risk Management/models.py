# models/risk_management.py

from app import db

class RiskManagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strategy_id = db.Column(db.Integer, db.ForeignKey('strategy.id'))
    stop_loss = db.Column(db.Float)
    take_profit = db.Column(db.Float)
    position_size = db.Column(db.Float)

    def __init__(self, strategy_id, stop_loss, take_profit, position_size):
        self.strategy_id = strategy_id
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.position_size = position_size

    # Additional methods as needed
