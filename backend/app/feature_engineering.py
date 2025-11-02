from typing import Optional
from sqlalchemy.orm import Session
from .models import Project, Builder
from .schemas import PropertyReport, ScoreBlock, SourceRef

def _cap(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def compute_report_for_project(db: Session, project: Project, builder: Optional[Builder]) -> PropertyReport:
    access = _cap((project.access_score or 0.0), 0, 10)
    infra = _cap((project.infra_uplift or 0.0), 0, 10)
    amenities = _cap((project.amenity_index or 0.0), 0, 10)
    aqi = _cap((project.aqi_score or 0.0), 0, 10)

    investment = round(0.35*access + 0.25*infra + 0.2*amenities + 0.2*(10 - aqi), 2)

    return PropertyReport(
        project_id=project.id,
        project_name=project.name,
        builder_name=builder.legal_name if builder else None,
        locality=project.locality,
        headline_psf=project.price_psf_p50,
        price_trend_12m=project.price_trend_12m,
        access=ScoreBlock(
            value=access, label="Access Score",
            rationale="AM/PM peak travel-time snapshots to major hubs (lower is better).",
            sources=[SourceRef(name="Google Distance Matrix")]
        ),
        infra=ScoreBlock(
            value=infra, label="Infra Uplift",
            rationale="Proximity to operational/planned metro stations.",
            sources=[SourceRef(name="BMRCL")]
        ),
        amenities=ScoreBlock(
            value=amenities, label="Amenity Index",
            rationale="Density of schools/hospitals/groceries within 1–3 km.",
            sources=[SourceRef(name="OpenStreetMap")]
        ),
        aqi=ScoreBlock(
            value=aqi, label="AQI Exposure (lower better)",
            rationale="Median AQI over last 90 days.",
            sources=[SourceRef(name="CPCB")]
        ),
        builder_risk=ScoreBlock(
            value=7.5, label="Builder Risk (higher better)",
            rationale="RERA compliance and on-time delivery (placeholder).",
            sources=[SourceRef(name="K-RERA")]
        ),
        investment_score=investment
    )
