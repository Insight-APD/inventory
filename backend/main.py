from fastapi import FastAPI
from database import Base, engine

app = FastAPI(title="Inventory System")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/items")
def get_items():
    return []