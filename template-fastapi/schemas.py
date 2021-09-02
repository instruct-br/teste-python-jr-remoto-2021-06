from typing import List


from pydantic import BaseModel


class PackageReleaseBase(BaseModel):

    name: str
    version: str


class PackageReleaseCreate(PackageReleaseBase):

    pass


class PackageRelease(PackageReleaseBase):
    id: int

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):

    name: str


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    packages_releases: List[PackageRelease] = []

    class Config:
        orm_mode = True
