from http import HTTPStatus
from fastapi impot FastAPI


app = FastAPI()


@app.post("/users")
def post_users():
    pass

@app.get("/superusers")
def get_superusers():
    pass

@app.get("/top-countries")
def get_top_countries():
    pass

@get.get("/team_insights")
def get_team_insights():
    pass

@get.get("/active-users-per-day")
def get_active_day_users():
    pass

@get.get("/evaluation")
def get_evaluation():
    pass