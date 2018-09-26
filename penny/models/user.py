from .abstract_base_model import AbstractBaseModel


class User(AbstractBaseModel):

    plural_name = 'Users'

    def __init__(self, id, email, password, first_name, last_name, favourite, updated_at):
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.favourite = favourite
        self.updated_at = updated_at

    def __str__(self):
        return "User(id='%s', email='%s', updated_at='%s')" % (
            self.id, self.email, self.updated_at)

    @classmethod
    def from_dict(cls, obj):
        if obj is None:
            return None

        return cls(obj.get('id'),
                   obj.get('email'),
                   obj.get('password'),
                   obj.get('first_name'),
                   obj.get('last_name'),
                   obj.get('favourite'),
                   obj.get('updated_at'))

    def to_dict(self):
        dict_value = {}
        dict_value['id'] = self.id
        dict_value['email'] = self.email
        dict_value['password'] = self.password
        dict_value['first_name'] = self.first_name
        dict_value['last_name'] = self.last_name
        dict_value['favourite'] = self.favourite
        dict_value['updated_at'] = self.updated_at
        return dict_value
