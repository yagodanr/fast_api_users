from fastapi import FastAPI

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str


users: list[User] = list()

app = FastAPI()


@app.get("/users")
def get_all_users():
    return users


@app.post("/users")
def create_user(user: User):
    global users
    users.append(user)
    return user


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for us in users:
        if us.id == user_id:
            return us

    return None
