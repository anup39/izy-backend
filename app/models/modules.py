from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class Modules(Model):
    __tablename__ = 'modules'
    module_id = Column(db.Integer, primary_key=True)
    module_name = Column(db.String)
    module_description = Column(db.String)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)
