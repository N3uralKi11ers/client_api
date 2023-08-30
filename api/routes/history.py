from fastapi import APIRouter
from typing import Optional, List
from schemas import TransactionBase, ProductBase
from crud import get_transactions

router = APIRouter()


@router.get(
    '/{consumer_name}/',
    name="All transactions",
    description="""
    This method returns all goods. 
    """,
    # response_model=List[TransactionBase],
)
def get_transactions_history(
    consumer_name: str,
    step: Optional[int] = None,
    limit: Optional[int] = None,
):
    if not limit:
        return get_transactions(consumer_name)
    
    return get_transactions(consumer_name)[step:step + limit]
