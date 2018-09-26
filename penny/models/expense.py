from .abstract_base_model import AbstractBaseModel
from google.cloud import datastore
from ..db import db_get_embedded_entity
import json


class Expense(AbstractBaseModel):

    plural_name = 'Expenses'

    def __init__(self, description, amount, involved, payor, id, type, percentage, shares):
        self.description = description
        self.amount = amount
        self.involved = involved
        self.payor = payor
        self.id = id
        self.type = type
        self.percentage = percentage
        self.shares = shares

    def __str__(self):
        return "Expense(description='%s', amount='%s', payor='%s')" % (
            self.description, self.amount, self.payor)

    @classmethod
    def from_dict(cls, obj):
        if obj is None:
            return None

        return cls(obj.get('description'),
                   obj.get('amount'),
                   obj.get('involved'),
                   obj.get('payor'),
                   obj.get('id'),
                   obj.get('type'),
                   obj.get('percentage'),
                   obj.get('shares'))

    def to_dict(self):
        dict_value = {}
        dict_value['description'] = self.description
        dict_value['amount'] = self.amount
        dict_value['involved'] = self.involved
        dict_value['payor'] = self.payor
        dict_value['id'] = self.id
        dict_value['type'] = self.type
        dict_value['percentage'] = json.loads(self.percentage)
        dict_value['shares'] = json.loads(self.shares)
        return dict_value

    def to_embedded(self):
        entity = db_get_embedded_entity('Expenses')
        entity['description'] = self.description
        entity['amount'] = self.amount
        entity['involved'] = self.involved
        entity['payor'] = self.payor
        entity['id'] = self.id
        entity['type'] = self.type
        entity['percentage'] = json.dumps(self.percentage)
        entity['shares'] = json.dumps(self.shares)
        return entity
