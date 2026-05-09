from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, int_pk, str_uniq  # используем твой str_uniq для email


class User(Base):
    """Пользователь системы"""
    id: Mapped[int_pk]

    # email используем как логин, он должен быть уникальным и проиндексированным
    email: Mapped[str_uniq]

    # Хранится хэш пароля, а не сам пароль (безопасность!)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    # Можно добавить флаг активности или роль, если в будущем будет админка
    is_active: Mapped[bool] = mapped_column(server_default="true")

    # Здесь можно добавить relationship, если захочешь быстро
    # подтягивать все данные юзера, но в DAO это лучше делать явно.
