from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship
from app.db import Base

class Users(BaseModel, Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)