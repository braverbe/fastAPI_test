from pydantic import BaseModel


class SProductAdd(BaseModel):
    name: str
    cost: int
    amount: int

class SProduct(SProductAdd):
    id: int

class SProductID(BaseModel):
    ok: bool = True
    product_id: int