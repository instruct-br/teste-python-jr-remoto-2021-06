$env:FASTAPI_ENV="development"
alembic upgrade head
uvicorn main:app --reload