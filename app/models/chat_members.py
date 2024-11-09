from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import BaseModel
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db import Base


class Chat_members(BaseModel, Base):
    __tablename__ = "chat_members"

    chat_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    chat_members_users = relationship("Users", back_populates="users_chat_members")

    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), nullable=False)
    chat_members_chats = relationship("Сhats", backref="chats_chat_members")

    __table_args__ = (
        UniqueConstraint("chat_user_id", "chat_id", name="unique_chat_user"),
    )
