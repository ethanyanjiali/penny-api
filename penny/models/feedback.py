from .abstract_base_model import AbstractBaseModel


class Feedback(AbstractBaseModel):

    plural_name = 'Feedback'

    def __init__(self, id, name, email, type, content):
        self.id = id
        self.name = name
        self.email = email
        self.type = type
        self.content = content

    def __str__(self):
        return "Feedback(id='%s', name='%s', type='%s')" % (
            self.id, self.name, self.type)

    @classmethod
    def from_dict(cls, obj):
        if obj is None:
            return None

        return cls(obj.get('id'),
                   obj.get('name'),
                   obj.get('email'),
                   obj.get('type'),
                   obj.get('content'))

    def to_dict(self):
        dict_value = {}
        dict_value['id'] = self.id
        dict_value['name'] = self.name
        dict_value['email'] = self.email
        dict_value['type'] = self.type
        dict_value['content'] = self.content
        return dict_value
