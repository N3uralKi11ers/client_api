from pydantic import BaseModel


class BaseTransaction(BaseModel):
    recipient: str
    description: str
    amount: float