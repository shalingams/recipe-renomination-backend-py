from fastapi import APIRouter, Depends, HTTPException
import dependencies

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["recipes"])
async def recipes():
    pass


@router.get("/{recipe_id}", tags=["recipes"])
async def recipe(recipe_id: str):
    pass

@router.post("/", tags=["recipes"])
async def store_recipe():
    pass


@router.delete("/{recipe_id}", tags=["recipes"])
def destroy_recipe(recipe_id: str):
    pass


@router.put("/{recipe_id}", tags=["recipes"])
async def update_recipe(recipe_id: str):
    pass


@router.post("/recommendations", tags=["recipes"])
async def recommendations():
    pass
