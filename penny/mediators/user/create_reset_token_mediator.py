from ..abstract_base_mediator import AbstractBaseMediator
from ...models.reset_token import ResetToken
from ...daos.reset_token_dao import ResetTokenDAO
from ...models.user import User
from ...daos.user_dao import UserDAO
from flask import jsonify
import datetime
import uuid
import requests


class CreateResetTokenMediator(AbstractBaseMediator):

    def __init__(self, request):
        self.request = request

    def run(self):
        payload = self.request.get_json()
        token_dict = payload['token']

        # Validate user object from request
        token = ResetToken.from_dict(token_dict)
        if token.email is None:
            response = jsonify(message="Missing email.", success=False)
            response.status_code = 400
            return response

        existing_user = UserDAO.readByEmail(token.email)

        if existing_user is None:
            response = jsonify(message="User with this email doesn't exist.", success=False)
            response.status_code = 400
            return response

        token.id = token.email
        tokenString = str(uuid.uuid4())[:6]
        token.token = tokenString
        token.expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        created_token = ResetTokenDAO.create(token)

        self.send_token_message(token.email, existing_user.first_name, tokenString)

        response = jsonify(success=True)
        response.status_code = 200
        return response

    def send_token_message(self, email, name, token):
        body = "Hello " + name + ", your password reset token is " + token + ". It will expire after 24 hours."
        # Use 3rd party mail service to send reset token
        return body
