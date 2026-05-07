from enum import unique

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped

from app.database import BASE, str_uniq, int_pk, str_null_true, str_indexed





class Product(BASE):
    id: Mapped[int_pk]
    name: Mapped[str]
    SKU: Mapped[str_indexed]
    shop_domain: Mapped[str_indexed]
    url: Mapped[str_uniq]
    category: Mapped[str_indexed]
    brand: Mapped[str_indexed]


    __table_args__ = (UniqueConstraint("SKU", "shop_domain", name="sku_shop_domain"),)

    def __repr__(self):
        return str(self)
