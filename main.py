from typing import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app:FastAPI):
    await delete_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

class SProductAdd(BaseModel):
    name: str
    cost: int
    amount: int

class SProductRead(SProductAdd):
    id: int


products = []
@app.post('/products')
async def add_product(
    product: Annotated[SProductAdd, Depends()],
):
    products.append(product)
    return {"ok": "True"}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}"}
