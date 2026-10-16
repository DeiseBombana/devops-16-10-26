from fastapi import FastAPI

APP = FastAPI()

@APP.get("/")
async def index():
    return {"servico": "gateway"}