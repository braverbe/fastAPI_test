from itertools import product

from sqlalchemy import select

from database import new_session, ProductOrm
from main import SProductAdd


class ProductRepository:
    @classmethod
    async def add_one(clscls, data: SProductAdd):
        async with new_session() as session:
            product_dict = data.model_dump()

            product = ProductOrm(**product_dict)
            session.add(product)
            await session.flush()
            await session.commit()
            return product.id


    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(ProductOrm)
            result = await session.execute(query)
            product_models = result.scalara().all()
            return product_models
