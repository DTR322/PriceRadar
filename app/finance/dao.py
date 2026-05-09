from app.dao.base import BaseDAO
from app.finance.models import Finance


class FinanceDAO(BaseDAO):
    model = Finance