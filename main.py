import uvicorn
from models import users
from schema import User
from app import app
from db import db


@app.post("/user/")
async def create_user(user: User):
    query = users.insert().values(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    user_id = await db.execute(query)
    return {"user_id": user_id}


@app.get("/user/{id}", response_model=User)
async def get_user(id: int):
    query = users.select().where(users.c.id == id)
    user = await db.fetch_one(query)
    return User(**user).dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
