from werkzeug.security import check_password_hash
from .daos.user_dao import UserDAO


def authenticate(email, password):
    existing_user = UserDAO.readByEmail(email)
    if existing_user is not None and \
            check_password_hash(existing_user.password, password):
        return existing_user


def identity(payload):
    user_id = payload['identity']
    user = UserDAO.read(user_id)
    return user
