from pydantic import BaseModel


class CardMIR(BaseModel):
    card_number: str
    color: str