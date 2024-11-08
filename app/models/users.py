from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship
from app.db import Base

class Users(BaseModel, Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    chat = relationship("chat_members", back_populates="user")
    message = relationship("chat_messages", back_populates="user_message")
