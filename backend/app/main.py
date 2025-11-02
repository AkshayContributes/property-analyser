from fastapi import FastAPI
from .api import router as api_router

app = FastAPI(title="Property Analyser API", version="0.1.0")
app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}
