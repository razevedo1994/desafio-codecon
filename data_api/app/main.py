from http import HTTPStatus
from typing import List

from fastapi import FastAPI
from pydantic import TypeAdapter

from app.schemas.schemas import User, UsersList

app = FastAPI()

database = dict()


@app.post("/users", status_code=HTTPStatus.CREATED, response_model=UsersList)
def post_users(users: List[User]):
    ta = TypeAdapter(List[User])
    database["users"] = ta.validate_python(users)

    return database


@app.get("/superusers")
def get_superusers():
    pass


@app.get("/top-countries")
def get_top_countries():
    pass


@app.get("/team_insights")
def get_team_insights():
    pass


@app.get("/active-users-per-day")
def get_active_day_users():
    pass


@app.get("/evaluation")
def get_evaluation():
    pass
