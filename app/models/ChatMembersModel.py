from sqlalchemy.orm import Mapped, mapped_column
from app.models.BaseModel import BaseModel
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db import Base


class ChatMembersModel(BaseModel, Base):
    __tablename__ = "ChatMembers"

    chat_user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"), nullable=False)
    ChatMembers_Users = relationship("Users", back_populates="Users_ChatMembers")

    chat_id: Mapped[int] = mapped_column(ForeignKey("Chats.id"), nullable=False)
    ChatMembers_Chats = relationship("Сhats", backref="Chats_ChatMembers")

    __table_args__ = (
        UniqueConstraint("chat_user_id", "chat_id", name="unique_chat_user"),
    )
