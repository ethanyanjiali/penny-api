from ..abstract_base_mediator import AbstractBaseMediator
from ...models.user import User
from ...daos.user_dao import UserDAO
from ...validators.user_validator import UserValidator
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
import datetime
import uuid

class CreateUserMediator(AbstractBaseMediator):

    def __init__(self, request):
        self.request = request

    def run(self):
        payload = self.request.get_json()
        user_dict = payload['user']

        # Validate user object from request
        user = User.from_dict(user_dict)
        valid, msg = UserValidator.validate_create(user=user)

        # If request is not valid return 400
        if not valid:
            response = jsonify(message=msg, success=False)
            response.status_code = 400
            return response

        # salt password
        user.password = generate_password_hash(user.password)
        # generate uuid
        user.id = str(uuid.uuid4())

        created_user = UserDAO.create(user)

        created_user.password = None

        response = jsonify(user=created_user.to_dict(), success=True)
        response.status_code = 200
        return response
