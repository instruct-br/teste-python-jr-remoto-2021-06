from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, schemas
from database import SessionLocal


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/projects/", response_model=List[schemas.Project])
def get_projects(db: Session = Depends(get_db)):
    projects = crud.get_projects(db)
    return projects


@app.get("/projects/{project_name}", response_model=schemas.Project)
def get_project_detail(project_name: str, db: Session = Depends(get_db)):
    # TODO
    # - Retornar informações do projeto
    return {"foo": "bar"}


@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    # TODO
    # - Processar pacotes recebidos
    # - Persistir as informações no banco
    return {"foo": "bar"}


@app.delete("/projects/{project_id}")
def delete_project(project_name: str, db: Session = Depends(get_db)):
    # TODO
    # - Apagar o projeto indicado
    return {"foo": "bar"}
