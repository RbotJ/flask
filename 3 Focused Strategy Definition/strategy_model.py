from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Strategy(db.Model):
    __tablename__ = 'strategies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    # Other relevant fields (parameters, indicators, etc.)

    def __repr__(self):
        return f'<Strategy {self.name}>'
