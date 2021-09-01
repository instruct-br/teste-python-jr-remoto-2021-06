from sqlalchemy.orm import Session, session
import models, schemas


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_projects(db: Session):
    return db.query(models.Project).all()


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(name=project.name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_packages_releases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PackageRelease).offset(skip).limit(limit).all()


def delete_project(db: Session, project: models.Project):
    db.delete(project)
    db.commit()
    return {"message": "Project deleted"}
