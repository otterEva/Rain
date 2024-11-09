from app.repositories.basedao import baseDAO
from app.models.users import Users

class Users_DAO(baseDAO):

    model = Users