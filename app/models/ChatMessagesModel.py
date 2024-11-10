from sqlalchemy.orm import Mapped, mapped_column
from app.models.BaseModel import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class ChatMessagesModel(BaseModel, Base):
    __tablename__ = "ChatMessages"

    message: Mapped[str] = mapped_column(nullable=False)

    chat_user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"), nullable=False)
    ChatMessages_Users = relationship("UsersModel", backref="Users_ChatMessages")

    chat_id: Mapped[int] = mapped_column(ForeignKey("Chats.id"), nullable=False)
    ChatMessages_Chats = relationship("ChatsModel", backref="Chats_ChatMessages")
