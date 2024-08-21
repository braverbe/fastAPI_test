from pydantic import BaseModel, ConfigDict


class SProductAdd(BaseModel):
    name: str
    cost: int
    amount: int

class SProduct(SProductAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SProductID(BaseModel):
    ok: bool = True
    product_id: int