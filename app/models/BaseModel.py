from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class BaseModel:
    id: Mapped[int] = mapped_column(primary_key=True)

    created_time: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    updated_time: Mapped[datetime] = mapped_column(
        nullable=False, default=func.now(), onupdate=func.now()
    )

    class Config:
        orm_mode = True
