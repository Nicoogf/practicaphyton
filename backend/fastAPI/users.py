"""Users"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# uvicorn users:app --reload
app = FastAPI()

# Entidad User


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Moure", surname="Dev",
         url="https://mouredev.com", age=27),
    User(id=3, name="Haakon", surname="Dahlberg",
         url="https://Haakon.com", age=20)
]


@app.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "Brais",
            "surname": "Moure",
            "url": "https:/moure.dev",
            "age": 35
        },
        {
            "name": "Moure",
            "surname": "Dev",
            "url": "https:/mouredev.com",
            "age": 27
        },
        {
            "name": "Haakon",
            "surname": "Dahlberg",
            "url": "https:/Haakon.com",
            "age": 20
        },

    ]


@app.get("/users")
async def users():
    return users_list


@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


@app.get("/user")
async def user(id: int):
    return search_user(id)


@app.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
       raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)
    return user


@app.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se actualizo el usuario"}
    else:
        return user


@app.delete("/user/{id}")
async def userDelete(id: int):

    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se actualizo el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "Usuario no encontrado"}
