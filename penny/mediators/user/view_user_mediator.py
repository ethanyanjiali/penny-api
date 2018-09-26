from ..abstract_base_mediator import AbstractBaseMediator
from ...models.user import User
from ...daos.user_dao import UserDAO
from flask import jsonify

class ViewUserMediator(AbstractBaseMediator):

    def __init__(self, request, current_identity):
        self.request = request
        self.current_identity = current_identity

    def run(self):
        returned_user = User.from_dict(self.current_identity.to_dict())
        returned_user.password = None
        response = jsonify(user=returned_user.to_dict(), success=True)
        return response
