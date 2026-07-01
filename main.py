from fastapi import FastAPI
from app.database.models import Base
from app.database.database import engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.get("/")
def root():
    return {"service":"is live"}