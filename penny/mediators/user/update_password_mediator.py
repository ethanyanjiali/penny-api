from ..abstract_base_mediator import AbstractBaseMediator
from ...models.user import User
from ...daos.user_dao import UserDAO
from ...daos.reset_token_dao import ResetTokenDAO
from ...validators.user_validator import UserValidator
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
import datetime
import iso8601
import pytz
import uuid

class UpdatePasswordMediator(AbstractBaseMediator):

    def __init__(self, request, current_identity):
        self.request = request
        self.current_identity = current_identity

    def run(self):
        payload = self.request.get_json()
        credentials = payload['credentials']

        if credentials.get('token') is None:
            # Validate old and new password
            valid, msg = UserValidator.validate_password_update(credentials, self.current_identity)

            # If request is not valid return 400
            if not valid:
                response = jsonify(message=msg, success=False)
                response.status_code = 400
                return response

            # Load existing user and put new password in
            existing_user = UserDAO.read(credentials.get('id'))
            existing_user.password = generate_password_hash(credentials.get('new_password'))
            updated_user = UserDAO.update(existing_user)

            response = jsonify(success=True)
            response.status_code = 200
            return response
        else:
            valid, msg = UserValidator.validate_password_reset(credentials)
            existing_user = UserDAO.readByEmail(credentials.get('email'))
            if existing_user is None:
                valid = False
                msg = "User with this email doesn't exist."

            existing_token = ResetTokenDAO.read(credentials.get('email'))
            if existing_token is None:
                valid = False
                msg = "Token doesn't exist."

            if existing_token.token != credentials.get('token'):
                valid = False
                msg = "Token is incorrect."

            if datetime.datetime.now(tz=pytz.utc) > iso8601.parse_date(str(existing_token.expiration_time)):
                valid = False
                msg = "Token is expired."

            # If request is not valid return 400
            if not valid:
                response = jsonify(message=msg, success=False)
                response.status_code = 400
                return response

            existing_user.password = generate_password_hash(credentials.get('new_password'))
            updated_user = UserDAO.update(existing_user)

            response = jsonify(success=True)
            response.status_code = 200
            return response
