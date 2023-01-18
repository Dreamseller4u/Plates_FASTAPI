from sqlalchemy.orm import Session
import models
import schemas


def get_plate(db: Session, plate_id: int):
    return db.query(models.Plate).filter(models.Plate.id == plate_id).first()


def create_plate(db: Session, plate: str):
    db_plate = models.Plate(plate_number=plate)
    db.add(db_plate)
    try:
        db.commit()
        db.refresh(db_plate)
    except Exception as e:
        return e
    return db_plate

# def get_users(db: Session, skip: int=0, limit: int=100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# def get_user_by_username(db: Session, username: str):
#     return db.query(models.User).filter(models.User.username == username).first()

# def create_user(db: Session, user: schemas.UserCreate):
#     hashed_pass = user.password + 'somehash'
#     db_user = models.User(username=user.username, hashed_password=hashed_pass)
#     db.add(db_user)
#     try:
#         db.commit()
#         db.refresh(db_user)
#     except Exception as e:
#         return e
#     return db_user
