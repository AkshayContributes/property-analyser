from fastapi import APIRouter, HTTPException
from .db import SessionLocal
from .models import Project, Builder
from .schemas import PropertyReport
from .feature_engineering import compute_report_for_project

router = APIRouter()

@router.get("/projects/{project_id}/report", response_model=PropertyReport)
def get_project_report(project_id: int):
    with SessionLocal() as db:
        project = db.get(Project, project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        builder = db.get(Builder, project.builder_id) if project.builder_id else None
        report = compute_report_for_project(db, project, builder)
        return report
