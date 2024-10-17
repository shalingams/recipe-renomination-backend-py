from fastapi import APIRouter

router = APIRouter()

@router.post("/update-account/{user_id}", tags=["users"])
def update_account(user_id: str):
    pass
