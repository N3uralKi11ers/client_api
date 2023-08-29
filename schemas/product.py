from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str 
    organization_id: int
    price: float
    consumer_name: float


class OrderedProduct(ProductBase):
    index: int


class ProductCashback(ProductBase):
    cashback: float