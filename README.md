# FastAPI URL Shortener

A scalable URL shortening service similar to **Bitly**, built using **FastAPI, MySQL, Redis, and SQLAlchemy**.

This project demonstrates backend system design concepts such as URL shortening, caching, database persistence, and API design.

---

# Features

- Shorten long URLs
- Redirect users using short codes
- Base62 short code generation
- Custom alias support
- Click tracking
- List all shortened URLs
- Stats endpoint
- Redis caching for faster redirects

---

# Tech Stack

Backend:
- FastAPI
- Python

Database:
- MySQL / MariaDB
- SQLAlchemy ORM

Cache:
- Redis

Server:
- Uvicorn

Validation:
- Pydantic

---

# Project Structure
fastapi-url-shortener
│
├── app
│ ├── main.py
│ ├── models.py
│ ├── crud.py
│ ├── schemas.py
│ ├── utils.py
│ └── redis_client.py
│
├── requirements.txt
├── README.md
└── .gitignore

---

# API Endpoints

### Create Short URL

POST `/shorten`

Request:{
“long_url”: “https://example.com”
}

Response:{
“long_url”: “https://example.com”,
“short_code”: “aB12Cd”,
“short_url”: “http://127.0.0.1:8001/aB12Cd”,
“clicks”: 0
}

---

### Redirect to Original URL

GET `/{code}`

Example:http://127.0.0.1:8001/aB12Cd
Redirects to the original URL.

---

### List All URLs

GET `/urls`

Returns all shortened URLs.

---

### Get URL Stats

GET `/stats/{code}`

Returns statistics for a specific short URL.

---

# System Architecture
Client

↓

FastAPI API Server

↓

Redis Cache (for fast redirects)

↓

MySQL Database (persistent storage)


### Flow

1. User sends a long URL.
2. Server generates a short code.
3. URL mapping is stored in MySQL.
4. Redis caches frequently accessed URLs.
5. Redirect requests check Redis first.
6. If not found in Redis, MySQL is queried.

---

# Base62 Short Code Generation

Short codes are generated using Base62 encoding.

Example:
ID → Base62

1 → b
10 → k
100 → bM

Benefits:

- Short URLs
- No collisions
- Scalable ID generation

---

# Run Locally

Clone repository

git clone https://github.com/abha-mandwale/fastapi-url-shortener.git

Navigate into project
cd fastapi-url-shortener

Create virtual environment
python -m venv myenv
source myenv/bin/activate

Install dependencies
pip install -r requirements.txt

Run server
uvicorn app.main:app –reload –port 8001
Open API docs

http://127.0.0.1:8001/docs

---


# Environment Variables

Create `.env` file

DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/url_shortener
BASE_URL=http://127.0.0.1:8001

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

---

# Example Short URL

Long URL:
https://google.com

Short URL:
http://127.0.0.1:8001/aB12Cd

---

# Future Improvements

- Expiry links
- User authentication
- Analytics dashboard
- QR code generation
- Rate limiting
- Docker support
- Kubernetes scaling

---

# Author

Abha Mandwale

GitHub:
https://github.com/abha-mandwale

---

# License

MIT License

---
