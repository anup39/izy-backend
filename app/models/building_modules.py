from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class BuildingModules(Model):
    __tablename__ = 'building_modules'
    building_module_id = Column(db.Integer, primary_key=True, autoincrement=True)
    module_id = Column(db.Integer)
    building_id = Column(db.String)
    active = Column(db.Integer)
