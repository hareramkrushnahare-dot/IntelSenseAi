# IntelSense AI - FastAPI microservice

This service is the AI engine for IntelSense AI. It accepts customer feedback, runs AI analysis, and returns structured intelligence payloads for the backend and dashboard.

## What it provides
- Sentiment analysis
- Emotion detection
- Aspect-based analysis
- Keyword extraction
- Topic detection
- Summary generation
- Explainability output
- Recommendation generation
- Health and analytics endpoints

## Quick start
1. Copy `.env.example` to `.env`.
2. Start the stack with Docker:
   - `docker compose up --build`
3. Open the API docs:
   - `http://localhost:8000/api/v1/docs`
4. Example prediction request:
   - `POST /api/v1/predict`

## Example payload
```json
{
  "text": "I love this product but support was slow.",
  "source": "web"
}
```

## Notes
- `USE_DUMMY_MODELS=true` uses built-in lightweight logic for local development.
- Set it to `false` to try real model loading paths when dependencies are available.
- Alembic is prepared for future migrations.
