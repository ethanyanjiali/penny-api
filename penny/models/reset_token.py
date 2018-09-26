from .abstract_base_model import AbstractBaseModel


class ResetToken(AbstractBaseModel):

    plural_name = 'ResetTokens'

    def __init__(self, id, email, token, expiration_time):
        self.id = id
        self.email = email
        self.token = token
        self.expiration_time = expiration_time

    def __str__(self):
        return "User(id='%s', token='%s', expiration_time='%s')" % (
            self.id, self.token, self.expiration_time)

    @classmethod
    def from_dict(cls, obj):
        if obj is None:
            return None

        return cls(obj.get('id'),
                   obj.get('email'),
                   obj.get('token'),
                   obj.get('expiration_time'))

    def to_dict(self):
        dict_value = {}
        dict_value['id'] = self.id
        dict_value['email'] = self.email
        dict_value['token'] = self.token
        dict_value['expiration_time'] = self.expiration_time
        return dict_value
