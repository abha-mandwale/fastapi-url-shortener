from sqlalchemy.orm import Session 
from . import models
from .utils import generate_short_code, encode_base62

def create_short_url(db: Session, long_url: str):
    existing_url = db.query(models.ShortURL).filter(
        models.ShortURL.long_url == long_url
    ).first()

    if existing_url:
        return existing_url

    code = generate_short_code()

    while db.query(models.ShortURL).filter(
        models.ShortURL.short_code == code
    ).first():
        code = encode_base62(url.id)
    url = models.ShortURL(
        long_url=long_url, 
        short_code=code
    
    )
    db.add(url)
    db.commit()
    db.refresh(url)
    return url

def get_by_code(db: Session, code: str):
    return db.query(models.ShortURL).filter(
        models.ShortURL.short_code == code
     ).first()

def get_all_urls(db: Session):
    return db.query(models.ShortURL).all()

