from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class PointsOfSales(Model):
    __tablename__ = 'points_of_sales'
    pos_id = Column(db.String, primary_key=True)
    pos_name = Column(db.String)
    store_id = Column(db.String, primary_key=True)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)



















