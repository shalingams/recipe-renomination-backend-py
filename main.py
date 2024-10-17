from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.post("/register")
def registration():
  pass

@app.post("/login")
def login():
  pass
  
@app.post("/reset-password")
def reset_password():
  pass

@app.post("/update-password")
def update_password():
  pass

@app.post("/update-account/{user_id}")
def update_account(user_id: str):
  pass

@app.get("/recipes")
def recipes():
  pass

@app.get("/recipes/{recipe_id}")
def recipe(recipe_id: str):
  pass
  
@app.post("/renominations")
def renominations():
  pass
