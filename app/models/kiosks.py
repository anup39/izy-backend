from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
# Alias common DB names
Column = db.Column
Model = db.Model

class Kiosks(Model):
    __tablename__ = 'kiosks'
    kiosk_id = Column(db.String, primary_key=True)
    kiosk_name = Column(db.String)
    description = Column(db.String)
    service_provider_id = Column(db.String)
    building_module_id = Column(db.Integer)
    building_id = Column(db.String)
    thumbnail_image_id =Column(UUID(as_uuid=True),default=uuid.uuid4)
    header_image_id = Column(UUID(as_uuid=True),default=uuid.uuid4)
    organisation_id = Column(db.String)
    service_provider_internal_id = Column(db.String)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)





