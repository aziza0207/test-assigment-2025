from fastapi import FastAPI, Depends, HTTPException
from project.database import Base, engine
from src.project import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)