from fastapi import APIRouter, Depends, HTTPException
import dependencies

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/register", tags=["auth"])
def registration():
    pass


@router.post("/login", tags=["auth"])
def login():
    pass


@router.post("/reset-password", tags=["auth"])
def reset_password():
    pass


@router.post("/update-password", tags=["auth"])
def update_password():
    pass
