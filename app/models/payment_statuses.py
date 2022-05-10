from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

# Alias common DB names
Column = db.Column
Model = db.Model


class PaymentStatuses(Model):
    __tablename__ = 'payment_statuses'
    payment_status_id = db.Column(db.Integer, primary_key=True)
    payment_status_name = Column(db.String)