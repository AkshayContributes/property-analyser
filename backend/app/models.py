from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
from .db import Base

class Builder(Base):
    __tablename__ = "builders"
    id = Column(Integer, primary_key=True)
    legal_name = Column(String, nullable=False)
    aka = Column(JSONB, default=list)
    rera_ids = Column(JSONB, default=list)
    hq_city = Column(String)
    risk_flags = Column(JSONB, default=list)
    source_refs = Column(JSONB, default=list)

    projects = relationship("Project", back_populates="builder")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    builder_id = Column(Integer, ForeignKey("builders.id"), nullable=True)
    name = Column(String, nullable=False)
    aka = Column(JSONB, default=list)
    rera_project_id = Column(String)
    status = Column(String)
    launch_date = Column(Date)
    promised_possession = Column(Date)
    oc_status = Column(String)
    locality = Column(String)
    ward_id = Column(String)
    centroid = Column(Geometry(geometry_type='POINT', srid=4326), nullable=True)
    price_psf_p50 = Column(Float)
    price_trend_12m = Column(Float)
    access_score = Column(Float)
    infra_uplift = Column(Float)
    amenity_index = Column(Float)
    aqi_score = Column(Float)
    risk_flags = Column(JSONB, default=list)
    source_refs = Column(JSONB, default=list)

    builder = relationship("Builder", back_populates="projects")
