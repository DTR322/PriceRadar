from fastapi import APIRouter
from app.finance.dao import FinanceDAO


router = APIRouter(
    prefix="/finance", tags=["работа с финансами"]
)


@router.get("/", summary="получить все финансы")
async def get_all_finance():
    return await FinanceDAO.find_all()