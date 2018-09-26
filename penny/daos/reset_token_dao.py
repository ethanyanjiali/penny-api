from ..db import db_create, db_read, db_update, db_list, db_list_by_filter, db_delete
from .abstract_base_dao import AbstractBaseDAO
from ..models.reset_token import ResetToken

class ResetTokenDAO(AbstractBaseDAO):

    @staticmethod
    def create(obj):
        dict_value = obj.to_dict()
        created_dict_value = db_create(ResetToken.plural_name, dict_value)
        return None if created_dict_value is None else ResetToken.from_dict(created_dict_value)

    @staticmethod
    def read(id):
        read_dict_value = db_read(ResetToken.plural_name, id)
        return None if read_dict_value is None else ResetToken.from_dict(read_dict_value)
