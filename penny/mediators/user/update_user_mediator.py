from ..abstract_base_mediator import AbstractBaseMediator
from ...models.user import User
from ...daos.user_dao import UserDAO
from ...validators.user_validator import UserValidator
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
import datetime
import uuid

class UpdateUserMediator(AbstractBaseMediator):

    def __init__(self, request, current_identity):
        self.request = request
        self.current_identity = current_identity

    def run(self):
        payload = self.request.get_json()
        user_dict = payload['user']

        # Validate user object from request
        user = User.from_dict(user_dict)
        valid, msg = UserValidator.validate_update(user=user, current_identity=self.current_identity)

        # If request is not valid return 400
        if not valid:
            response = jsonify(message=msg, success=False)
            response.status_code = 400
            return response

        # Load existing user and put password in
        existing_user = UserDAO.read(user.id)
        user.password = existing_user.password

        updated_user = UserDAO.update(user)

        updated_user.password = None

        response = jsonify(user=updated_user.to_dict(), success=True)
        response.status_code = 200
        return response
