from pydantic import BaseModel, HttpUrl

class ShortenRequest(BaseModel):
    long_url: HttpUrl

class ShortenUrlResponse(BaseModel):
    long_url: str
    short_code: str
    short_url: str
    clicks: int
