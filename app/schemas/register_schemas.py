from pydantic import BaseModel, EmailStr

class SUserData(BaseModel):
    email: EmailStr
    password: str