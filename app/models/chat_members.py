from app.database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import BaseModel
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class Chat_members(BaseModel, Base):
    __tablename__ = 'chat_members'

    chat_user_id : Mapped[int] = mapped_column(ForeignKey('users.id'), nullable = False)
    user = relationship('users', back_populates='chat')

    chat_id : Mapped[int] = mapped_column(ForeignKey('chats.id'), nullable = False)
    chatting = relationship('chats', back_populates='chat_refference')

    __table_args__ = (UniqueConstraint('chat_user_id', 'chat_id', name='unique_chat_user'),)