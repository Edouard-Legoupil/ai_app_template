# Vibe Coding Guide

## Code Quality Principles
- Follow PEP8 (Python) and Airbnb/Prettier (JS/TS)
- Docstrings for functions/classes (Python)
- JSDoc for React components
- Typed interfaces for models/services
- No magic numbers or duplicate logic

## AI Agent Orchestration
- Decouple agents from workflows
- Prefer engine-based extension (CrewAI/LangChain)
- State and context explicit, serializable

## Database & Vector Store
- All schema changes via Alembic migrations
- Set up pgvector extensions for AI/ML

## FastAPI + React Integration
- Use routers for API modularity
- Serve React static in production only
- Dev via Vite with proxy

## Security
- Always hash secrets in config (use .env)
- Never commit sensitive keys
- Use HTTPS certs for public deployment

## Testing
- Keep tests in /backend/tests and use pytest
- Mock external APIs for reproducibility

## Style
- Single-responsibility for components/services
- Prefer functional/react hooks
- All new APIs include OpenAPI docs
- UI styled for accessibility and vibe

---

For deeper workflow standards and more advanced orchestration, extend this guide.
