from sqlalchemy.orm import Mapped, mapped_column
from app.models.BaseModel import BaseModel
from app.db import Base


class ChatsModel(BaseModel, Base):
    __tablename__ = "Chats"

    chat_name: Mapped[str | None] = mapped_column(default=None)
