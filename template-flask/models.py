from sqlalchemy import Column, String

from database import Base


class Project(Base):
    __tablename__ = 'projects'

    id = Column(String, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
            return f'<Project {self.name}>'
