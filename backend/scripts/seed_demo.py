#!/usr/bin/env python3
from sqlalchemy.orm import Session
from app.db import SessionLocal, engine, Base
from app.models import Builder, Project

Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    b = Builder(legal_name="Prestige Estates", aka=["Prestige"])
    db.add(b); db.flush()
    p = Project(
        builder_id=b.id, name="Prestige Lakeside Habitat", locality="Whitefield",
        price_psf_p50=10500, price_trend_12m=6.0,
        access_score=8.0, infra_uplift=7.5, amenity_index=7.0, aqi_score=3.0
    )
    db.add(p)
    db.commit()
print("Seeded demo builder/project.")
