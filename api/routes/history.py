from fastapi import APIRouter
from typing import Optional, List
from schemas import TransactionBase, ProductBase

router = APIRouter()

fake_db = [

]

@router.get(
    '/{consumer_name}/',
    name="All transactions",
    description="""
    This method returns all goods. 
    """,
    response_model=List[TransactionBase],
)
def get_transactions_history(
    consumer_name: str,
    limit: Optional[int],
):
    return [
        TransactionBase(
            recipient="qwerty",
            description="lrhlw lhrewlh wel",
            amount=123.123,
        ),
        TransactionBase(
            recipient="qwerty",
            description="lrhlw lhrewlh wel",
            amount=123.123,
        ),
        TransactionBase(
            recipient="qwerty",
            description="lrhlw lhrewlh wel",
            amount=123.123,
        )
    ]


@router.get(
    '/{consumer_name}/products',
    name="All products",
    response_model=List[ProductBase],
)
def get_products_history(

):
    return []