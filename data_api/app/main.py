from http import HTTPStatus
from fastapi import FastAPI
from app.schemas.schemas import Users


app = FastAPI()


@app.post("/users", response_model=Users)
def post_users():
    pass

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