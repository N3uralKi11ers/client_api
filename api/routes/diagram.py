from fastapi import APIRouter
from typing import List

from crud import diagram_allocation
from schemas import Diagram

router = APIRouter()


@router.get(
    '/{consumer_name}/',
    name="User diagram",
    description="""
    This method returns data for pie chart in Statistics screen.
    """,
    response_model=Diagram,
)
def get_user_diagram(
    consumer_name: str,
):
    return diagram_allocation(consumer_name)