from fastapi import APIRouter, status, Depends
from typing import List
from .. import utils, schemas, models
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix = "/users",
    tags = ["Users"]
)

# All users
@router.get("/", response_model = List[schemas.UserOut], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
   users = db.query(models.User)
   return users

# Create user
@router.post("/", response_model = schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user