from typing import List
from typing_extensions import TypedDict
from datetime import date
from uuid import UUID


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

class Users(TypedDict):
    id: UUID
    nome: str
    idade: int
    score: int
    ativo: bool
    pais: str
    equipe: Team
    logs: List[Logs]