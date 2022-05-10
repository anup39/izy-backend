from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class Buildings(Model):
    __tablename__ = 'buildings'
    building_id = Column(db.String, primary_key=True)
    building_name = Column(db.String)
    licensee_id = Column(db.String)
    user_app_self_registration = Column(db.Integer)
    tenant_registration_code = Column(db.Integer, unique=True)
    private_building = Column(db.Integer)
    country = Column(db.String)
    country_code = Column(db.String)
    postal_number = Column(db.String)
    address = Column(db.String)
    city = Column(db.String)
    latitude = Column(db.Float)
    longitude = Column(db.Float)
    square_meters = Column(db.Integer)
    number_of_users = Column(db.Integer)
    number_of_floors = Column(db.Integer)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)
