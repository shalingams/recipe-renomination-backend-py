from fastapi import FastAPI, Depends
from pydantic import BaseModel
import routers
import dependencies
import routers.recipe
import routers.users
import routers.auth


app = FastAPI(dependencies=[Depends(dependencies.get_query_token)])

app.include_router(routers.recipe.router)
app.include_router(routers.users.router)
app.include_router(routers.auth.router)

@app.get("/")
def read_root():
  return {"Hello": "World"}
