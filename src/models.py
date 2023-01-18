from sqlalchemy import Column, String, Integer
from database import Base


class Plate(Base):
    __tablename__ = 'plates'

    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, unique=True, index=True)

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key = True, index = True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String, unique=True, index=True)
