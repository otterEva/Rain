from pydantic import BaseModel
from datetime import datetime

class BaseSchema(BaseModel):
    id:int
    created_time: datetime
    updated_time: datetime

    class Config:
        orm_mode = True