from ..db import db_create, db_read, db_update, db_list, db_list_by_filter, db_delete
from .abstract_base_dao import AbstractBaseDAO
from ..models.event import Event

class EventDAO(AbstractBaseDAO):

    @staticmethod
    def create(obj):
        dict_value = obj.to_dict()
        created_dict_value = db_create(Event.plural_name, dict_value)
        return None if created_dict_value is None else Event.from_dict(created_dict_value)

    @staticmethod
    def read(id):
        read_dict_value = db_read(Event.plural_name, id)
        return None if read_dict_value is None else Event.from_dict(read_dict_value)

    @staticmethod
    def update(obj):
        dict_value = obj.to_dict()
        updated_dict_value = db_update(Event.plural_name, dict_value)
        return None if updated_dict_value is None else Event.from_dict(updated_dict_value)
