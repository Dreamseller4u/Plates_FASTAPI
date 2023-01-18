from pydantic import BaseModel


class PlateBase(BaseModel):
    plate_number:   str


class PlateCreate(PlateBase):
    pass


class Plate(PlateBase):
    id: int

    class Config:
        orm_mode = True

# class UserBase(BaseModel):
#     username: str

# class UserCreate(UserBase):
#     password : str

# class User(UserBase):
#     id: int

#     class Config:
#         orm_mode=True
