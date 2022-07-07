from app import db
from datetime import datetime
from sqlalchemy.sql import func

class Route(db.Model):
    __tablename__ = 'patente'
    __table_args__ = {'schema': 'tables'}
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.now, nullable=False, server_default=func.now())
    
    def __init__(self, placa):
        self.placa = placa