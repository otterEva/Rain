from app.repositories.BaseDAO import BaseDAO
from app.models.UsersModel import UsersModel
from app.schemas.UserSchemas import UsersSchema


class UsersDAO(BaseDAO):
    model = UsersModel
    schema = UsersSchema


users_dao = UsersDAO()
