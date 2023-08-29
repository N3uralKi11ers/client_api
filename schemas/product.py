from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    price: float
    cashback: float


class OrderedProduct(ProductBase):
    index: int