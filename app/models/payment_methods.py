from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

# Alias common DB names
Column = db.Column
Model = db.Model


class PaymentMethods(Model):
    __tablename__ = 'payment_methods'
    payment_method_id = db.Column(db.Integer, primary_key=True)
    payment_method_name = Column(db.String)
    cash_payment = Column(db.Integer, nullable=False)