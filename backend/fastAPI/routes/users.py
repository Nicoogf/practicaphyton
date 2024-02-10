"""Users"""

# pylint: disable=missing-function-docstring

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# uvicorn users:app --reload
router = APIRouter()

# Entidad User


class User(BaseModel):
    """
    Clase tipo Usuario
    """
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


@router.get("/usersjson")
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


@router.get("/users")
async def users_get():
    """
    Obtiene la lista de usuarios.
    """
    return users_list


@router.get("/user/{id}")
async def user_get(user_id: int):
    """
    Informacion sobre un solo usuario
    """
    return search_user(user_id)


@router.get("/user")
async def user_gets(user_id: int):
    """
    Informacion sobre un solo usuario
    """
    return search_user(user_id)


@router.post("/user/", response_model=User, status_code=201)
async def user_post(user: User):
    """
    Agregar usuario
    """
    if isinstance(search_user(user.id), User):
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)
    return user


@router.put("/user/")
async def user_put(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se actualizo el usuario"}
    else:
        return user


@router.delete("/user/{id}")
async def user_delete(ide: int):

    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == ide:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se actualizo el usuario"}


def search_user(ide: int):
    users = filter(lambda user: user.id == ide, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "Usuario no encontrado"}
