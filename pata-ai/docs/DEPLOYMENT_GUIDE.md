# Production Deployment Guide

FastAPI container deployment with Uvicorn and PostgreSQL.

## Docker Run
```bash
docker build -t pata-ai-backend ./backend
docker run -d -p 8000:8000 --env-file .env pata-ai-backend
```
