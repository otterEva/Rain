from app.database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import EmailStr
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship

class Users(BaseModel, Base):
    __tablename__ = 'users'

    email : Mapped[EmailStr] = mapped_column(unique=True, nullable = False)
    hashed_password : Mapped[str] = mapped_column(nullable = False)

    chat = relationship('chat_members', back_populates='user')
    message = relationship('chat_messages', back_populates='user_message')
