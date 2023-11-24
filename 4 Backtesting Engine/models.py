from app import db

class BacktestResult(db.Model):
    __tablename__ = 'backtest_results'

    id = db.Column(db.Integer, primary_key=True)
    strategy_name = db.Column(db.String(50))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    performance_metric = db.Column(db.Float)
    
    # Other relevant fields...
