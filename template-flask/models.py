from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    package_releases = relationship('PackageRelease', backref='project')

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
            return f'<Project {self.name}>'


class PackageRelease(Base):
    __tablename__ = 'package_release'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(String)

    project_id = Column(Integer, ForeignKey('project.id'))

    def __init__(self, id=None, name=None, version=None, project_id=None):
        self.id = id
        self.name = name
        self.version = version
        self.project_id = project_id

    def __repr__(self):
            return f'<Project {self.name}>'
