from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from db import schemas, crud, models
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users")
def get_all_users(db: Session=Depends(get_db)):
    return crud.get_users(db)


@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session=Depends(get_db)):

    return crud.create_user(db, user)


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session=Depends(get_db)):
    return crud.get_user_by_id(db, user_id)
