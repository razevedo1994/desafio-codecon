from datetime import date
from typing import List
from uuid import UUID

from pydantic import BaseModel
from typing_extensions import TypedDict


class Projects(TypedDict):
    nome: str
    concluido: bool


class Team(TypedDict):
    nome: str
    lider: bool
    projetos: List[Projects]


class Logs(TypedDict):
    date: date
    action: str


class User(TypedDict):
    id: UUID
    nome: str
    idade: int
    score: int
    ativo: bool
    pais: str
    equipe: Team
    logs: List[Logs]


class UsersList(BaseModel):
    users: List[User]
