from .abstract_base_model import AbstractBaseModel
from .expense import Expense


class Event(AbstractBaseModel):

    plural_name = 'Events'

    def __init__(self, id, name, people, expenses, updated_at):
        self.id = id
        self.name = name
        self.people = people
        self.expenses = expenses
        self.updated_at = updated_at

    def __str__(self):
        return "Event(id='%s', name='%s', updated_at='%s')" % (
            self.id, self.name, self.updated_at)

    @classmethod
    def from_dict(cls, obj):
        if obj is None:
            return None

        return cls(obj.get('id'),
                   obj.get('name'),
                   obj.get('people'),
                   obj.get('expenses'),
                   obj.get('updated_at'))

    def to_dict(self):
        dict_value = {}
        dict_value['id'] = self.id
        dict_value['name'] = self.name
        dict_value['people'] = self.people
        dict_value['expenses'] = self.expenses
        dict_value['updated_at'] = self.updated_at
        return dict_value
