from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    packages_releases = relationship("PackageRelease", back_populates="project")


class PackageRelease(Base):
    __tablename__ = "packages_releases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    version = Column(String, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="packages_releases")
