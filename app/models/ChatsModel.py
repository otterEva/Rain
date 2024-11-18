from sqlalchemy.orm import Mapped, mapped_column
from app.models.BaseModel import BaseModel
from app.db import Base


class ChatsModel(BaseModel, Base):
    __tablename__ = "Chats"

    chat_name: Mapped[str | None] = mapped_column(default=None)

    def __str__(self):
        return f"chat_id: {self.id}"

    def __repr__(self):
        return f"chat_id: {self.id}"
