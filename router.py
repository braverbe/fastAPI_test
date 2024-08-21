from typing import Annotated

from fastapi import APIRouter, Depends

from repository import ProductRepository
from schemas import SProductAdd

router = APIRouter(
    prefix='/products'
)

@router.post('/products')
async def add_product(
    product: Annotated[SProductAdd, Depends()],
):
    await ProductRepository.add_one(product)
    return {"ok": "True"}

@router.get("/")
async def det_products():
    products = await ProductRepository.find_all()
    return {"products": products}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}"}