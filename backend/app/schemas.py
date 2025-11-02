from pydantic import BaseModel
from typing import List, Optional

class SourceRef(BaseModel):
    name: str
    url: Optional[str] = None
    last_updated: Optional[str] = None

class ScoreBlock(BaseModel):
    value: float = 0.0
    label: str = ""
    rationale: str = ""
    sources: List[SourceRef] = []

class PropertyReport(BaseModel):
    project_id: int
    project_name: str
    builder_name: Optional[str] = None
    locality: Optional[str] = None
    headline_psf: Optional[float] = None
    price_trend_12m: Optional[float] = None
    access: ScoreBlock
    infra: ScoreBlock
    amenities: ScoreBlock
    aqi: ScoreBlock
    builder_risk: ScoreBlock
    investment_score: float = 0.0
