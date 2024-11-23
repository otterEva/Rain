from pydantic import EmailStr
from app.schemas.BaseSchemas import BaseSchema


class UsersSchema(BaseSchema):
    email: EmailStr
    hashed_password: str
