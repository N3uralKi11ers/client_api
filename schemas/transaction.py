from pydantic import BaseModel

class TransactionBase(BaseModel):
    product_title: str
    price: float
    datetime: str