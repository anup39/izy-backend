from app import db
from sqlalchemy.dialects.postgresql import UUID

# Alias common DB names
Column = db.Column
Model = db.Model


class BuildingGraphicProfiles(Model):
    __tablename__ = 'building_graphic_profiles'
    building_id = Column(db.String, primary_key=True)
    primary_color_hex = Column(db.String)
    accent_color_hex = Column(db.String)
    background_color_hex = Column(db.String)
    header_image_id = Column(UUID(as_uuid=True))
