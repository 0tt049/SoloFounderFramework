---
name: scaffolding-python-backends
description: Generates a strictly typed Python and FastAPI backend skeleton following Clean Architecture and test-driven design principles. Trigger this when setting up a new service, bootstrapping database models, initializing Alembic migrations, or defining FastAPI endpoint routes.
allowed-tools: [Read, Write, Edit, Glob]
---

# Scaffolding Python Backends

## Goal
To scaffold a production-grade, highly scalable Python backend using FastAPI, package manager `uv`, ORM `SQLAlchemy 2.0` (with full async support and Alembic migrations), strict `mypy` typing, and clean separation of concerns.

## When to Use This Skill
- When creating a new microservice or API module.
- When initiating database tables or ORM models.
- When configuring linting rules or code checkers (`ruff`, `mypy`).

### Do Not Use This Skill For:
- Frontend layout scaffolding (e.g. React or Vue components).
- One-off scripting and data loading scripts without framework structure.

## Plan-Validate-Execute Workflow
1. **Plan (Folder Setup):**
   - Lay out the project structure:
     ```text
     app/
     ├── api/             # Routers, endpoints, schemas
     ├── domain/          # Core business entities, models
     ├── infrastructure/  # DB engine, alembic, repositories
     └── tests/           # TDD unit/integration tests
     ```
2. **Validate (Checks & Rules):**
   - Validate that `pyproject.toml` contains `uv` run configurations, strict `mypy` configuration, and `ruff` rules.
   - Run verification checkers:
     ```bash
     uv pip install -r requirements.txt
     mypy app/
     ruff check app/
     ```
3. **Execute (Code Gen):**
   - Save the base template code for the API router and core async DB configs.

## Design Rules & Guidelines

### Layer Insulation
- Domain layers must remain absolutely isolated. They are never allowed to import routers or network structures.
- Use repositories to abstract database actions from the API controllers.

### Strict Typing Requirements
- Enforce strict typing. All functions must declare param types and explicit return annotations.
- Never use generic `Any` types; use TypedDict or appropriate Union/Generic alternatives.

## Example Implementation Checklist
Copy and use this checklist for scaffolding backend services:

- [ ] Create the standard app folder structure (`api/`, `domain/`, `infrastructure/`, `tests/`).
- [ ] Write configured `pyproject.toml` and setup `uv` package settings.
- [ ] Code base async database connector using SQLAlchemy 2.0.
- [ ] Initialize Alembic with async migration template configurations.
- [ ] Run `ruff` and `mypy` to verify that scaffolding is clean.
- [ ] Verify test correctness by designing a dummy testing endpoint.
