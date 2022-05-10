from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class Licensees(Model):
    __tablename__ = 'licensees'
    licensee_id = Column(db.String, primary_key=True)
    licensee_name = Column(db.String)
    organisation_id = Column(db.String)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)
