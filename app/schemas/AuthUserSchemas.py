from pydantic import BaseModel, EmailStr


class SAuthUser(BaseModel):
    email: EmailStr
    password: str
