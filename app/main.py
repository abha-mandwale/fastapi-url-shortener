from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

from .database import SessionLocal, engine
from . import models, schemas, crud
from .redis_client import redis_client

try:
    from .redis_client import redis_client
except Exception:
    redis_client = None


load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  

@app.post("/shorten/", response_model=schemas.ShortenUrlResponse)
def shorten_url(data: schemas.ShortenRequest, db: Session = Depends(get_db)):
    url = crud.create_short_url(db, str(data.long_url))

    return {
        "long_url": url.long_url,
        "short_code": url.short_code,
        "short_url": f"{BASE_URL}/{url.short_code}",
        "clicks": url.clicks
    }

@app.get("/urls")
def list_urls(db: Session = Depends(get_db)):
    urls = crud.get_all_urls(db)
    return urls

@app.get("/stats/{code}")
def url_stats(code: str, db: Session = Depends(get_db)):
    url = crud.get_by_code(db, code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {
        "long_url": url.long_url,
        "short_code": url.short_code,
        "short_url": f"{BASE_URL}/{url.short_code}",
        "clicks": url.clicks
    }

@app.get("/{code}")
def redirect_to_long_url(code: str, db: Session = Depends(get_db)):
    cached = None
    if redis_client:
        try:
            cached = redis_client.get(f"short:{code}")
        except Exception:
            cached = None

    if cached:
        return RedirectResponse(url=cached)

    url = crud.get_by_code(db, code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    url.clicks += 1
    db.commit()

    redis_client.setex(f"short:{code}", 3600, url.long_url)

    return RedirectResponse(url=url.long_url)

