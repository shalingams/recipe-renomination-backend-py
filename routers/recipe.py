from fastapi import APIRouter

router = APIRouter()

@router.get("/recipes", tags=["recipes"])
async def recipes():
    pass


@router.get("/recipes/{recipe_id}", tags=["recipes"])
async def recipe(recipe_id: str):
    pass

@router.post("/recipes", tags=["recipes"])
async def store_recipe():
    pass


@router.delete("/recipes/{recipe_id}", tags=["recipes"])
def destroy_recipe(recipe_id: str):
    pass


@router.put("/recipes/{recipe_id}", tags=["recipes"])
async def update_recipe(recipe_id: str):
    pass


@router.post("/renominations", tags=["recipes"])
async def renominations():
    pass
