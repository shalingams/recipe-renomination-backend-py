from fastapi import APIRouter, Depends, HTTPException
import dependencies

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.put("/{user_id}", tags=["users"])
def update_account(user_id: str):
    pass
