from fastapi import APIRouter
from typing import Tuple

from crud import get_cashback

router = APIRouter()


@router.get(
    '/{consumer_name}/',
    name="All cashbacks",
    description="""
    This method returns all cashbacks. 
    """,
    response_model=Tuple[str],
)
def get_user_cashback(
    consumer_name: str,
):
    return get_cashback(consumer_name)