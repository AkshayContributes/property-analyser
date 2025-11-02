# Property Analyser — MVP (Bengaluru Pilot)

**Goal:** Ship a public-facing Property Report API for Bengaluru with a minimal data spine.

## Stack
- Backend: FastAPI (Python 3.11)
- DB: Postgres 16 + PostGIS
- Infra: Docker Compose
- (Optional) Frontend stub: Next.js placeholder

## Quick start

### 1) Copy env
```
cp backend/.env.example backend/.env
```

### 2) Start DB + API
```
docker compose up --build
```
API docs: http://localhost:8000/docs

### 3) Initialize DB schema
In a separate terminal:
```
docker compose exec db psql -U postgres -d property_analyser -f /sql/01_init.sql
```

### 4) Seed demo data (optional)
```
docker compose exec api python backend/scripts/seed_demo.py
```

---

## What’s included
- `backend/sql/01_init.sql` — PostGIS + core tables for builders, projects, amenities, metro, AQI, travel-time snapshots
- `backend/app/feature_engineering.py` — Access Score, Amenity Index, Infra Uplift, AQI Score (simple v0 formulas)
- `backend/app/resolver.py` — entity resolution stub (name/geo based)
- `backend/app/api.py` — `/projects/{id}/report` returning a report card (with source refs)
- `backend/scripts/ingest_osm.py` — OSM Overpass amenity pull (schools/hospitals/groceries/parks) for project centroids
- `backend/scripts/ingest_rera_placeholder.py` — structure + notes for K-RERA ingest (fill with actual parsing as per site/API availability)
- `backend/scripts/compute_features.py` — orchestrates feature computation into Gold tables

> Note: Respect all robots.txt/ToS for third-party sources. Prefer official datasets/APIs.

---

## Next steps
- Wire Google Distance Matrix snapshots (AM/PM peaks) and store to `travel_time_snapshot`
- Implement real K-RERA ingestion
- Add PDF export endpoint
- Build a simple Next.js page (search → report)
