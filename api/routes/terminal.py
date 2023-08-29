from fastapi import APIRouter
import random

router = APIRouter()

@router.get(
    '/',
    name="Biometry auth",
    description="""
    Returns true or false
    """
)
def auth_user():
    res = bool(random.getrandbits(1))
    return {"status" : res}