from fastapi import FastAPI
from src import grphql_app, init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()  

app.include_router(grphql_app, prefix="/graphql")
