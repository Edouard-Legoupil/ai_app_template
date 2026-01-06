# AI App Boilerplate Backend

Welcome to the FastAPI + CrewAI backend!

## Purpose

- Exposes REST API endpoints for document search, document generation using YAML templates, review generation (via CrewAI orchestration), and decision automation.
- Integrates vector stores, PDF/document chunking.
- Supports robust agent-automation and modern AI workflows.

## Opinionated, Template-Driven Design

This backend follows a **template-driven, opinionated architecture** for document automation and process orchestration:

- **Templates as YAML**: All document generation flows are driven by YAML-based templates. Each template defines a set of sections and precise instructions for each section, making the process auditable, reproducible, and highly customizable by design.
- **Declarative Structure**: Templates are stored in `src/api/v1/template/`, allowing teams to clearly define what constitutes a document, version template logic, and maintain standards as your organization evolves.
- **Advantages**:
  - _Traceable_: All generated outputs can be matched to their template source for easy review and compliance.
  - _Customizable_: New document types or policies are onboarded by simply adding or updating YAML files—no code changes required.
  - _Opinionated_: Minimizes ambiguity in automation and agent orchestration by enforcing structure. This leads to robust output, clear team collaboration, and dramatically reduced edge-case complexity. Your automation is always explicit, never hidden in sprawling conditional code or static configuration.

## Workflow: Template-Driven Document Generation

1. **Templates stored in `src/api/v1/template/` as YAML files**
    - Example: `climate_policy.yaml`
    - Each YAML file defines a document structure, with named sections and instructions for each section.

2. **API Endpoints:**
    - `GET /api/v1/templates` — lists all available templates, their sections, and instructions.
    - `POST /api/v1/document/generate` — generates a document based on a template name; runs CrewAI for each section.

3. **How it works:**
    - Client invokes `/api/v1/document/generate` with a template name and context.
    - Backend loads the template, runs CrewAI for each section, and returns a full document (sections+content).

## Structure

- `src/` — Source code and modules for the app (main.py, api routes, models, agents).
- `src/api/v1/template/` — Stores YAML templates for document generation.
- `alembic/` — Database migrations and schema evolution.
- `.env.example` — Environment variable template for secrets and config.
- `requirements.txt` — All dependencies (see: `pip install -r requirements.txt`).

## Database Migration (Alembic)

- Alembic manages DB schema changes. See `alembic.ini` for config.
- Migrations stored in `alembic/versions/`.
- Configured for SQLAlchemy models in `src/models`.

### To run migrations

1. Fill out `.env` with your correct `DATABASE_URL`
2. Run:  
   ```sh
   alembic upgrade head
   ```
   from the `backend/` folder.

### To create a new migration

```sh
alembic revision --autogenerate -m "add new table/field"
```

## Running the App

- Activate venv:  
  ```sh
  source ../venv/bin/activate
  ```
- Install requirements:  
  ```sh
  pip install -r requirements.txt
  ```
- Start server:  
  ```sh
  uvicorn src.main:app --host 0.0.0.0 --port 8000
  ```

## Document Generation Example

1. Add a YAML template to `src/api/v1/template/` (see `climate_policy.yaml`).
2. Call the API:
   ```sh
   curl -X POST http://localhost:8000/api/v1/document/generate \
      -H 'Content-Type: application/json' \
      -d '{"template_name": "climate_policy.yaml", "context": "Context text here"}'
   ```
3. Get a full document with CrewAI-generated content for each section.

## Environment and Secrets

- `.env.example` provided; copy to `.env` and set your keys:

  ```
  cp .env.example .env
  ```

## Contact

For questions/issues, see docs in `potential_process.md` or reach out via your team's preferred support channel.

---
