from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class Organisations(Model):
    __tablename__ = 'organisations'
    organisation_id = Column(db.String, primary_key=True)
    organisation_name = Column(db.String, nullable=False)
    organisation_number = Column(db.String, nullable=False, unique=True)
    address = Column(db.String)
    postal_code = Column(db.String)
    city = Column(db.String)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)
