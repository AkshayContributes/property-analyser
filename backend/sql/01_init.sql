-- Enable PostGIS and create core tables
CREATE EXTENSION IF NOT EXISTS postgis;

-- Builders
CREATE TABLE IF NOT EXISTS builders (
  id SERIAL PRIMARY KEY,
  legal_name TEXT NOT NULL,
  aka JSONB DEFAULT '[]',
  rera_ids JSONB DEFAULT '[]',
  hq_city TEXT,
  risk_flags JSONB DEFAULT '[]',
  source_refs JSONB DEFAULT '[]'
);

-- Projects
CREATE TABLE IF NOT EXISTS projects (
  id SERIAL PRIMARY KEY,
  builder_id INT REFERENCES builders(id),
  name TEXT NOT NULL,
  aka JSONB DEFAULT '[]',
  rera_project_id TEXT,
  status TEXT,
  launch_date DATE,
  promised_possession DATE,
  oc_status TEXT,
  locality TEXT,
  ward_id TEXT,
  centroid GEOGRAPHY(POINT, 4326),
  price_psf_p50 DOUBLE PRECISION,
  price_trend_12m DOUBLE PRECISION,
  access_score DOUBLE PRECISION,
  infra_uplift DOUBLE PRECISION,
  amenity_index DOUBLE PRECISION,
  aqi_score DOUBLE PRECISION,
  risk_flags JSONB DEFAULT '[]',
  source_refs JSONB DEFAULT '[]'
);

-- Amenities snapshot
CREATE TABLE IF NOT EXISTS amenities_snapshot (
  id SERIAL PRIMARY KEY,
  project_id INT REFERENCES projects(id),
  radius_km DOUBLE PRECISION NOT NULL,
  schools INT DEFAULT 0,
  hospitals INT DEFAULT 0,
  parks INT DEFAULT 0,
  groceries INT DEFAULT 0,
  last_refreshed_at TIMESTAMP DEFAULT now()
);

-- Travel time snapshot
CREATE TABLE IF NOT EXISTS travel_time_snapshot (
  id SERIAL PRIMARY KEY,
  project_id INT REFERENCES projects(id),
  ts_bucket TEXT CHECK (ts_bucket IN ('AM_peak','PM_peak')),
  to_airport_min DOUBLE PRECISION,
  to_cbd_min DOUBLE PRECISION,
  to_techpark1_min DOUBLE PRECISION,
  to_techpark2_min DOUBLE PRECISION,
  to_techpark3_min DOUBLE PRECISION,
  created_at TIMESTAMP DEFAULT now()
);

-- AQI snapshot
CREATE TABLE IF NOT EXISTS aqi_snapshot (
  id SERIAL PRIMARY KEY,
  project_id INT REFERENCES projects(id),
  window_days INT DEFAULT 90,
  median_aqi DOUBLE PRECISION,
  bad_air_days_pct DOUBLE PRECISION,
  last_refreshed_at TIMESTAMP DEFAULT now()
);

-- Metro stations (geometry only)
CREATE TABLE IF NOT EXISTS metro_stations (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  status TEXT, -- planned/operational
  geom GEOGRAPHY(POINT, 4326)
);

CREATE INDEX IF NOT EXISTS idx_projects_centroid ON projects USING GIST (centroid);
CREATE INDEX IF NOT EXISTS idx_metro_geom ON metro_stations USING GIST (geom);
