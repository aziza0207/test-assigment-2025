from fastapi import FastAPI, Depends, HTTPException
from .database import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()