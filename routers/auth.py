from fastapi import APIRouter

router = APIRouter()

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
