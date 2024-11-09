from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class Chat_messages(BaseModel, Base):
    __tablename__ = "chat_messages"

    message: Mapped[str] = mapped_column(nullable=False)

    chat_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    chat_messages_users = relationship("Users", back_populates="users_chat_messages")

    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), nullable=False)
    chat_messages_chats = relationship("Chats", back_populates="chats_chat_messages")
