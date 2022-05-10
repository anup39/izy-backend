from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

# Alias common DB names
Column = db.Column
Model = db.Model


class OrderLines(Model):
    __tablename__ = 'order_lines'
    order_line_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parent_order_id = Column(UUID(as_uuid=True), nullable=False)
    order_line_reference = Column(UUID(as_uuid=True))
    product_id = Column(UUID(as_uuid=True))
    product_name = Column(db.String)
    product_price_ex_vat = Column(db.Float)
    vat_rate = Column(db.Float)
    product_price_incl_vat = Column(db.Float)
    quantity = Column(db.Float)
    total_amount_ex_vat = Column(db.Float)
    total_amount_incl_vat = Column(db.Float)
    total_subsidy_amount_incl_vat = Column(db.Float)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)