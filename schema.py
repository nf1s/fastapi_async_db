from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True

