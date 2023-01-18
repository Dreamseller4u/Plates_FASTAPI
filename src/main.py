from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import crud
import models
import schemas
import utils

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return {'access_token': form_data.password + 'somehash'}
    # user = crud.get_user_by_username(db, username=form_data.username)
    # if user is None:
    #     raise HTTPException(status_code=401, detail='Not authenticated')
    # return {
    #     'access_token': user.hashed_password,
    # }


@app.get('/PLATE/GET')
async def read_plate(plate_id: int, token: str = Depends(oauth), db: Session = Depends(get_db)):
    db_plate = crud.get_plate(db, plate_id=plate_id)
    if db_plate is None:
        raise HTTPException(status_code=404, detail='Plate not found')
    if token is None:
        raise HTTPException(status_code=401, detail='Not authenticated')
    return db_plate


@app.get("/PLATE/GENERATE")
async def plate_gen(amount: str = '1', token: str = Depends(oauth)):
    if token is None:
        raise HTTPException(status_code=401, detail='Not authenticated')
    return utils.generate_plate_number(amount)


@app.post('/PLATE/ADD')
async def add_plate_number(plate: str, db: Session = Depends(get_db), token: str = Depends(oauth)):
    correct_plate = utils.check_plate(plate)
    if correct_plate is None:
        raise HTTPException(
            status_code=401, detail='Incorect plate numer. Please input value as X999XX in cyrillic')
    return crud.create_plate(db, plate)


# @app.post('/users/', response_model=schemas.User)
# async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
