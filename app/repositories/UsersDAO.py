from app.repositories.BaseDAO import BaseDAO
from app.models.UsersModel import UsersModel


class UsersDAO(BaseDAO):
    model = UsersModel
