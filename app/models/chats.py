from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship
from app.db import Base


class Chats(BaseModel, Base):
    __tablename__ = "chats"

    chat_name: Mapped[str | None] = mapped_column(default=None)
