from sqlalchemy.orm import Mapped, mapped_column
from app.models.BaseModel import BaseModel
from app.db import Base


class UsersModel(BaseModel, Base):
    __tablename__ = "Users"

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
