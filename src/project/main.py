from fastapi import FastAPI
from src.project.router import router
from src.project.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
