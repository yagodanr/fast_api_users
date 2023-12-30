from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User:
    db_user = models.User(
        username=user.username,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int) -> schemas.User:
    return db.get(models.User, user_id)

def get_users(db: Session, skip: int=0, limit: int=100) -> list[schemas.User]:
    return db.query(models.User).offset(skip).limit(limit).all()
