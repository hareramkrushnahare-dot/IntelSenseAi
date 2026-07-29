# IntelSense AI - Enterprise Architecture Structure

This document defines the complete production-ready folder and file structure for the IntelSense AI microservice.

## Purpose
IntelSense AI is an enterprise-grade AI customer intelligence platform that receives customer feedback from the Spring Boot backend, performs advanced NLP analysis, stores AI insights in a shared MySQL database, and returns structured JSON responses.

## Architecture Principles
- Clean Architecture
- Domain-Driven Design
- SOLID Principles
- Separation of concerns across layers
- Scalable for high-throughput inference workloads
- Extensible for future AI and domain features

## Top-Level Structure

```text
ai-service/
├── app/
├── alembic/
├── docker/
├── docs/
├── scripts/
├── tests/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
├── requirements.txt
└── main.py
```

## Application Layer

```text
app/
├── api/
│   ├── __init__.py
│   ├── v1/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   ├── prediction.py
│   │   ├── analytics.py
│   │   ├── summary.py
│   │   ├── recommendation.py
│   │   ├── admin.py
│   │   └── batch.py
│   └── deps/
│       ├── __init__.py
│       └── auth.py
├── core/
│   ├── __init__.py
│   ├── app.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── logging.py
│   └── lifecycle.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── environment.py
│   └── secrets.py
├── settings/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   ├── redis.py
│   ├── ai.py
│   ├── logging.py
│   ├── security.py
│   ├── monitoring.py
│   └── storage.py
├── dependencies/
│   ├── __init__.py
│   ├── database.py
│   ├── redis.py
│   ├── auth.py
│   └── container.py
├── domain/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── prediction.py
│   │   ├── feedback.py
│   │   ├── insight.py
│   │   ├── recommendation.py
│   │   └── audit_log.py
│   ├── value_objects/
│   │   ├── __init__.py
│   │   ├── sentiment_result.py
│   │   ├── emotion_result.py
│   │   ├── aspect_result.py
│   │   ├── keyword_result.py
│   │   ├── topic_result.py
│   │   └── summary_result.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── prediction_orchestrator.py
│   │   ├── recommendation_service.py
│   │   └── analytics_service.py
│   └── repositories/
│       ├── __init__.py
│       ├── prediction_repository.py
│       ├── feedback_repository.py
│       ├── insight_repository.py
│       └── audit_repository.py
├── application/
│   ├── __init__.py
│   ├── use_cases/
│   │   ├── __init__.py
│   │   ├── predict_feedback.py
│   │   ├── analyze_batch.py
│   │   ├── generate_summary.py
│   │   ├── generate_recommendations.py
│   │   └── health_check.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── prediction_service.py
│   │   ├── batch_service.py
│   │   ├── analytics_service.py
│   │   └── report_service.py
│   └── ports/
│       ├── __init__.py
│       ├── prediction_repository_port.py
│       ├── cache_port.py
│       ├── ai_model_port.py
│       └── storage_port.py
├── infrastructure/
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   │   ├── engine.py
│   │   ├── migrations.py
│   │   └── health.py
│   ├── persistence/
│   │   ├── __init__.py
│   │   ├── sqlalchemy_prediction_repository.py
│   │   ├── sqlalchemy_feedback_repository.py
│   │   ├── sqlalchemy_insight_repository.py
│   │   └── sqlalchemy_audit_repository.py
│   ├── cache/
│   │   ├── __init__.py
│   │   ├── redis_client.py
│   │   ├── cache_repository.py
│   │   └── key_builder.py
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── local_storage.py
│   │   ├── s3_storage.py
│   │   └── upload_handler.py
│   ├── messaging/
│   │   ├── __init__.py
│   │   ├── event_publisher.py
│   │   └── event_consumer.py
│   └── security/
│       ├── __init__.py
│       ├── jwt_handler.py
│       ├── token_validator.py
│       └── encryption.py
├── ai/
│   ├── __init__.py
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   ├── normalizer.py
│   │   ├── tokenizer.py
│   │   ├── language.py
│   │   ├── validator.py
│   │   └── stopwords.py
│   ├── embeddings/
│   │   ├── __init__.py
│   │   ├── sentence_embedder.py
│   │   └── embedding_service.py
│   ├── sentiment/
│   │   ├── __init__.py
│   │   ├── predictor.py
│   │   └── schema.py
│   ├── emotion/
│   │   ├── __init__.py
│   │   ├── predictor.py
│   │   └── schema.py
│   ├── aspect/
│   │   ├── __init__.py
│   │   ├── predictor.py
│   │   └── schema.py
│   ├── keywords/
│   │   ├── __init__.py
│   │   ├── extractor.py
│   │   └── schema.py
│   ├── topics/
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── schema.py
│   ├── summarization/
│   │   ├── __init__.py
│   │   ├── summarizer.py
│   │   └── schema.py
│   ├── recommendation/
│   │   ├── __init__.py
│   │   ├── generator.py
│   │   └── schema.py
│   │   └── rules.py
│   ├── explainability/
│   │   ├── __init__.py
│   │   ├── shap_service.py
│   │   └── explanation_schema.py
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── inference_pipeline.py
│   │   ├── batch_pipeline.py
│   │   └── orchestration.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── registry.py
│   │   ├── model_loader.py
│   │   ├── model_config.py
│   │   └── fallback_models.py
│   ├── versioning/
│   │   ├── __init__.py
│   │   ├── model_version.py
│   │   └── registry_store.py
│   └── monitoring/
│       ├── __init__.py
│       ├── health.py
│       ├── metrics.py
│       └── probes.py
├── middleware/
│   ├── __init__.py
│   ├── request_logging.py
│   ├── timing.py
│   ├── cors.py
│   ├── exception_handler.py
│   ├── rate_limit.py
│   └── security_headers.py
├── schemas/
│   ├── __init__.py
│   ├── common.py
│   ├── prediction.py
│   ├── analytics.py
│   ├── batch.py
│   ├── health.py
│   └── recommendation.py
├── services/
│   ├── __init__.py
│   ├── prediction_service.py
│   ├── batch_service.py
│   ├── analytics_service.py
│   ├── summary_service.py
│   ├── recommendation_service.py
│   └── monitoring_service.py
├── repositories/
│   ├── __init__.py
│   ├── prediction_repository.py
│   ├── feedback_repository.py
│   ├── insight_repository.py
│   ├── analytics_repository.py
│   └── audit_repository.py
├── models/
│   ├── __init__.py
│   ├── prediction.py
│   ├── feedback.py
│   ├── emotion_result.py
│   ├── aspect_result.py
│   ├── summary.py
│   ├── keyword.py
│   ├── topic.py
│   ├── recommendation.py
│   ├── audit_log.py
│   └── model_registry.py
├── workers/
│   ├── __init__.py
│   ├── tasks.py
│   ├── batch_worker.py
│   ├── model_refresh.py
│   ├── report_worker.py
│   └── scheduler.py
├── cache/
│   ├── __init__.py
│   ├── redis_client.py
│   ├── cache_service.py
│   ├── ttl_config.py
│   └── invalidation.py
├── monitoring/
│   ├── __init__.py
│   ├── metrics.py
│   ├── probes.py
│   ├── dashboards.py
│   └── alerts.py
├── metrics/
│   ├── __init__.py
│   ├── counter.py
│   ├── histogram.py
│   └── gauge.py
├── events/
│   ├── __init__.py
│   ├── base.py
│   ├── prediction_event.py
│   ├── batch_event.py
│   └── model_event.py
├── logging/
│   ├── __init__.py
│   ├── formatter.py
│   ├── handlers.py
│   └── context.py
├── security/
│   ├── __init__.py
│   ├── auth.py
│   ├── roles.py
│   └── permissions.py
├── storage/
│   ├── __init__.py
│   ├── uploads.py
│   └── artifacts.py
├── uploads/
│   ├── __init__.py
│   └── README.md
├── utils/
│   ├── __init__.py
│   ├── datetime.py
│   ├── json.py
│   ├── files.py
│   ├── hashing.py
│   ├── uuid.py
│   └── validation.py
├── common/
│   ├── __init__.py
│   ├── enums.py
│   ├── constants.py
│   └── types.py
└── main.py
```

## Infrastructure and Project Support

```text
alembic/
├── versions/
├── env.py
└── README.md

docker/
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
└── .dockerignore

docs/
├── architecture.md
├── api.md
├── deployment.md
├── runbook.md
└── ADRs/

scripts/
├── setup.sh
├── migrate.sh
├── seed_data.sh
└── healthcheck.sh

tests/
├── unit/
├── integration/
├── e2e/
├── fixtures/
└── conftest.py
```

## File-by-File Responsibility Notes

### Root Files
- main.py: Application entrypoint for production and local execution.
- pyproject.toml: Project metadata and dependency declarations for Python packaging.
- requirements.txt: Explicit runtime dependency list for deployment and CI.
- Dockerfile: Container build definition for the AI service.
- docker-compose.yml: Local orchestration for FastAPI, MySQL, and Redis.
- README.md: Project overview, setup instructions, and architecture summary.
- .env.example: Sample environment configuration for local development.

### app/api/ files
- health.py: Exposes readiness and liveness endpoints.
- prediction.py: Handles inbound prediction requests from the Spring Boot backend.
- analytics.py: Exposes analytics and reporting endpoints.
- summary.py: Provides summary generation endpoints.
- recommendation.py: Exposes recommendation-related APIs.
- admin.py: Provides operational and administrative endpoints.
- batch.py: Supports batch inference jobs.

### app/core/ files
- app.py: Defines the application bootstrap and middleware registration.
- constants.py: Centralizes shared constants and status values.
- exceptions.py: Contains domain and service-level exception definitions.
- logging.py: Configures structured logging using Loguru.
- lifecycle.py: Defines startup and shutdown lifecycle hooks.

### app/config/ and app/settings/ files
- settings.py: Loads and validates environment configuration.
- environment.py: Manages environment-specific configuration.
- secrets.py: Contains secret configuration handling.
- database.py, redis.py, ai.py, logging.py, security.py, monitoring.py, storage.py: Provide typed configuration for each subsystem.

### app/domain/ files
- prediction.py, feedback.py, insight.py, recommendation.py, audit_log.py: Define domain entities.
- sentiment_result.py, emotion_result.py, aspect_result.py, keyword_result.py, topic_result.py, summary_result.py: Define immutable value objects for AI outputs.
- prediction_orchestrator.py: Coordinates domain-level prediction workflows.

### app/application/ files
- predict_feedback.py: Application use case for single feedback prediction.
- analyze_batch.py: Use case for batch inference.
- generate_summary.py: Use case for summary generation.
- generate_recommendations.py: Use case for business recommendation generation.
- health_check.py: Use case for service health operations.

### app/infrastructure/ files
- database/session.py and engine.py: Manage SQLAlchemy sessions and engine initialization.
- base.py: Declares the base declarative model.
- persistence modules: Implement concrete repository adapters for SQLAlchemy.
- cache modules: Provide Redis integration and cache policy abstractions.
- storage modules: Manage file and artifact persistence.

### app/ai/ files
- preprocessing modules: Clean and normalize incoming text.
- embeddings modules: Generate dense vector representations.
- sentiment/emotion/aspect/keywords/topics/summarization/recommendation/explainability modules: Implement AI pipeline components.
- pipelines modules: Orchestrate the multi-model inference workflow.
- models modules: Register, load, and version models.
- monitoring modules: Expose AI runtime health and performance metrics.

### app/workers/ files
- tasks.py: Declares background processing task entrypoints.
- batch_worker.py: Executes background batch inference jobs.
- model_refresh.py: Handles model refresh and version switch logic.
- report_worker.py: Produces scheduled analytics and reports.
- scheduler.py: Controls task scheduling and periodic execution.

### app/monitoring/ and app/metrics/ files
- metrics.py, histogram.py, gauge.py: Define system and AI metrics.
- probes.py and alerts.py: Monitor health and trigger operational responses.

### app/events/ files
- prediction_event.py, batch_event.py, model_event.py: Define domain events used for async workflows.

### app/security/ files
- auth.py, roles.py, permissions.py: Define enterprise authentication and authorization boundaries.

### app/storage/ and app/uploads/ files
- uploads.py, artifacts.py: Manage AI-generated files and temporary uploads.

### app/utils/ and app/common/ files
- Shared helper modules and common type definitions used across the service.

### alembic/ files
- env.py: Alembic migration environment configuration.
- versions/: Stores migration scripts.

### tests/ files
- unit/ : Unit tests for services, repositories, and AI components.
- integration/ : Integration tests for database and Redis interactions.
- e2e/ : End-to-end tests for the FastAPI API.
- fixtures/ : Shared test fixtures.

## Layering Summary
- Presentation Layer: app/api/
- Application Layer: app/application/
- Domain Layer: app/domain/
- Infrastructure Layer: app/infrastructure/
- AI Layer: app/ai/
- Shared Layer: app/common/, app/utils/, app/config/, app/settings/
- Utilities: app/utils/
- Configuration: app/config/, app/settings/
- Monitoring: app/monitoring/, app/metrics/
- Workers: app/workers/
