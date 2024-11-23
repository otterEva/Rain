from pydantic import BaseModel
from typing import Literal


class HealthcheckSchema(BaseModel):
    status: Literal["OK"]
    version: str

    class Config:
        orm_mode = True
