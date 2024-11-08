from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import Model
from sqlalchemy.orm import relationship


class Chats(Model, Base):
    __tablename__ = "chats"

    chat_name: Mapped[str | None] = mapped_column(default=None)
    chat_refference = relationship("chat_members", back_populates="chatting")
    messaging = relationship("chat_messages", back_populates="chat_message")
