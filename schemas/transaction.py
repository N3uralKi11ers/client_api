from pydantic import BaseModel


class TransactionBase(BaseModel):
    recipient: str
    description: str
    amount: float