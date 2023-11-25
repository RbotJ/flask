from app import db

class TradePerformance(db.Model):
    __tablename__ = 'trade_performance'
    
    id = db.Column(db.Integer, primary_key=True)
    strategy_id = db.Column(db.Integer, nullable=False)
    total_return = db.Column(db.Float, nullable=False)
    win_ratio = db.Column(db.Float, nullable=False)
    drawdown = db.Column(db.Float, nullable=False)
    # Other relevant fields

    def __repr__(self):
        return f'<TradePerformance {self.id}>'
