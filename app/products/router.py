from fastapi import APIRouter
from app.products.dao import ProductDAO


router = APIRouter(
    prefix="/products", tags=["работа с товарами"]
)


@router.get("/", summary="получить все товары")
async def get_all_products():
    return await ProductDAO.find_all_products()