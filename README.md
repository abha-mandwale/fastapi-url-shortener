# FastAPI URL Shortener
A simple URL shortener built with FastAPI, MySQL, and Redis.

## Features
- Shorten long URLs
- Redirect using short code
- Base62 short code generation
- Custom alias support
- Click tracking
- URL listing
- Stats endpoint
- Optional Redis caching

## Tech Stack
- FastAPI
- MySQL / MariaDB
- SQLAlchemy
- Pydantic
- Uvicorn
- Redis 
 
## Setup

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies
4. Create `.env`
5. Create MySQL database
6. Run the app

```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001

### 7. `.env` example
```md
DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/url_shortener
BASE_URL=http://127.0.0.1:8001
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

## API Endpoints

- POST `/shorten`
- GET `/urls`
- GET `/stats/{code}`
- GET `/{code}`

## Example Request

POST /shorten

{
  "long_url": "https://example.com",
  "custom_alias": "example"
}

## Future Improvements
- Expiry links
- User authentication
- QR code generation
- Analytics dashboard
- Docker support
- Rate limiting