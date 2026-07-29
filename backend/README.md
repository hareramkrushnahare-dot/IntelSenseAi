# IntelSense AI Backend

Spring Boot backend for the IntelSense AI platform.

## Features
- JWT-ready security scaffold
- Feedback submission endpoint
- AI service client for FastAPI predictions
- MySQL-backed persistence

## Run locally
1. Start MySQL locally with the shared database credentials:
   - username: Tanishg16
   - password: Tanish@2009
   - database: intelsense_ai
2. Start the AI service:
   - `cd ai-service && source .venv/bin/activate && uvicorn app.main:app --reload`
3. Start the backend:
   - `mvn spring-boot:run`

## Endpoints
- `GET /api/health`
- `POST /api/feedback`
