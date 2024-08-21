from pydantic import BaseModel


class SProductAdd(BaseModel):
    name: str
    cost: int
    amount: int

class SProductRead(SProductAdd):
    id: int