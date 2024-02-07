"""Users"""
from fastapi import FastAPI
from pydantic import BaseModel

# uvicorn users:app --reload
app = FastAPI()

# Entidad User

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list= [
    User(name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(name="Moure", surname="Dev", url="https://mouredev.com", age=27),
    User(name="Haakon", surname="Dahlberg", url="https://Haakon.com", age=20)
]

@app.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "Brais",
            "surname": "Moure",
            "url": "https:/moure.dev",
            "age" : 35
        },
        {
            "name": "Moure",
            "surname": "Dev",
            "url": "https:/mouredev.com",
            "age" : 27
        },
        {
            "name": "Haakon" , 
            "surname" :"Dahlberg" ,
            "url": "https:/Haakon.com",
            "age" : 20
         },

    ]

@app.get("/users")
async def userclass():
    return users_list