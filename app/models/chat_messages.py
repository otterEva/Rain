from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import Model
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Chat_messages(Model, Base):
    __tablename__ = "chat_messages"

    message: Mapped[str] = mapped_column(nullable=False)

    chat_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user_message = relationship("users", back_populates="message")

    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), nullable=False)
    chat_message = relationship("chats", back_populates="messaging")
