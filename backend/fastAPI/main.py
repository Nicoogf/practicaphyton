"""FastApi"""
# pylint: disable=missing-function-docstring
from fastapi import FastAPI
from routers import users # [import-error]


app = FastAPI()

app.include_router(users.router)


@app.get("/")
async def root():
    return "holaFastAPI"


@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}
