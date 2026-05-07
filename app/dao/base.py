from sqlalchemy import select
from app.database import async_session


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            products = await session.execute(query)
            return products.scalars().all()
