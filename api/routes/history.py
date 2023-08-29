from fastapi import APIRouter
from typing import Optional

router = APIRouter()

fake_db = [
    
]

@router.get(
    '/',
    name="All ",
    description="""
    This method returns all goods. 
    """
)
def get_history(
    limit: Optional[int],
):
    return {"qwerty" : 12345}