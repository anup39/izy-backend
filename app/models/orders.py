from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

# Alias common DB names
Column = db.Column
Model = db.Model


class Orders(Model):
    __tablename__ = 'orders'
    order_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    store_id = Column(db.String, nullable=False)
    pos_id = Column(db.String, nullable=False)
    order_reference = Column(UUID(as_uuid=True))
    total_amount_ex_vat = Column(db.Float)
    total_vat_amount = Column(db.Float)
    total_amount_incl_vat = Column(db.Float)
    payment_method_id = Column(db.Integer)
    payment_status_id = Column(db.Integer)
    cash_order = Column(db.Integer)
    user_id = Column(UUID(as_uuid=True))
    user_email = Column(db.String)
    user_full_name = Column(db.String)
    ordered_by = Column(UUID(as_uuid=True))
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)