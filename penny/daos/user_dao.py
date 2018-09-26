from ..db import db_create, db_read, db_update, db_list, db_list_by_filter, db_delete
from .abstract_base_dao import AbstractBaseDAO
from ..models.user import User

class UserDAO(AbstractBaseDAO):

    @staticmethod
    def create(obj):
        dict_value = obj.to_dict()
        created_dict_value = db_create(User.plural_name, dict_value)
        return None if created_dict_value is None else User.from_dict(created_dict_value)

    @staticmethod
    def read(id):
        read_dict_value = db_read(User.plural_name, id)
        return None if read_dict_value is None else User.from_dict(read_dict_value)

    @staticmethod
    def update(obj):
        dict_value = obj.to_dict()
        updated_dict_value = db_update(User.plural_name, dict_value)
        return None if updated_dict_value is None else User.from_dict(updated_dict_value)

    @staticmethod
    def delete(id):
        db_delete(User.plural_name, id)

    @staticmethod
    def list():
        dict_list = db_list(User.plural_name)

        if dict_list is None or len(dict_list) == 0:
            return []

        user_list = map(lambda x: User.from_dict(x), dict_list)
        return user_list

    @staticmethod
    def readByEmail(email):
        dict_list = db_list_by_filter(User.plural_name,
                                      'email', '=', email)
        if dict_list is None or len(dict_list) == 0:
            return None

        return User.from_dict(dict_list[0])
