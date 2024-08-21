from typing import Annotated

from fastapi import APIRouter, Depends

from repository import ProductRepository
from schemas import SProduct, SProductAdd, SProductID

router = APIRouter(
    prefix='/products',
    tags=['Товары']
)

@router.post('/')
async def add_product(
    product: Annotated[SProductAdd, Depends()],
) -> SProductID:
    product_id = await ProductRepository.add_one(product)
    return {"ok": "True", "product_id": product_id}

@router.get("/")
async def det_products() -> list[SProduct]:
    products = await ProductRepository.find_all()
    return {"data": products}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}"}