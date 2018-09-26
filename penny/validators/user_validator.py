import re
from ..daos.user_dao import UserDAO
from werkzeug.security import check_password_hash

class UserValidator:

    @staticmethod
    def validate_credentials(credentials):
        if credentials is None:
            return False, "Credentials is not a valid JSON."

        if credentials['email'] is None or not re.match(r"[^@]+@[^@]+\.[^@]+", credentials['email']):
            return False, "Please provide a valid email."

        if credentials['password'] is None or len(credentials['password']) < 8:
            return False, "Please provide a minimum 8 characters password."

        return True, "Success"

    @staticmethod
    def validate_create(user):
        valid, msg = UserValidator.validate_base_fields(user)
        if valid:
            valid, msg = UserValidator.validate_password(user.password)
        if valid:
            valid, msg = UserValidator.validate_not_exist(user)
        return valid, msg

    @staticmethod
    def validate_update(user, current_identity):
        valid, msg = UserValidator.validate_base_fields(user)
        if valid:
            valid, msg = UserValidator.validate_identity_match(
                user, current_identity)
        if valid:
            valid, msg = UserValidator.validate_exist(user)
        return valid, msg

    @staticmethod
    def validate_password(password):
        if password is None or len(password) < 8:
            return False, "Please provide a minimum 8 characters password."

        return True, "Success"

    @staticmethod
    def validate_identity_match(user, current_identity):
        if user.id is None:
            return False, "Please provide an id for the user."

        if user.id != current_identity.id:
            return False, "You're not allowed to update user with id " + user.id + "."

        return True, "Success"

    @staticmethod
    def validate_base_fields(user):
        if user is None:
            return False, "User is not a valid JSON."

        if user.email is None or not re.match(r"[^@]+@[^@]+\.[^@]+", user.email):
            return False, "Please provide a valid email."

        if user.first_name is None:
            return False, "Please provide a first name for this user."

        if len(user.first_name) is 0:
            return False, "Please provide a non-empty first name."

        if user.last_name is None:
            return False, "Please provide a last name for this user."

        if len(user.last_name) is 0:
            return False, "Please provide a non-empty last name."

        return True, "Success"

    @staticmethod
    def validate_not_exist(user):
        existing_user = UserDAO.readByEmail(user.email)
        if existing_user is None:
            return True, "Success"
        else:
            return False, "User with email " + user.email + " already exist."

    @staticmethod
    def validate_exist(user):
        existing_user = UserDAO.read(user.id)
        if existing_user is None:
            return False, "User with id " + user.id + " doesn't exist."
        else:
            return True, "Success"

    @staticmethod
    def validate_password_reset(credentials):
        valid = True
        if valid and credentials.get('new_password') is None:
            valid = False
            msg = "Please provide valid new password."
            
        if valid and credentials.get('token') is None:
            valid = False
            msg = "Token is invalid."

        if valid and credentials.get('email') is None:
            valid = False
            msg = "Please provide valid new email."

        if valid:
            valid, msg = UserValidator.validate_password(credentials.get('new_password'))

        return valid, msg


    @staticmethod
    def validate_password_update(credentials, current_identity):
        valid = True
        if credentials.get('id') is None:
            valid = False
            msg = "Please provide valid id."

        if valid and credentials.get('old_password') is None:
            valid = False
            msg = "Please provide valid old password."

        if valid and credentials.get('new_password') is None:
            valid = False
            msg = "Please provide valid new password."
            
        if valid and credentials.get('id') != current_identity.id:
            valid = False
            msg = "You're not allowed to update password for user with id " + credentials.get('id') + "."

        if valid:
            existing_user = UserDAO.read(credentials.get('id'))
            if existing_user is None:
                valid = False
                msg = "User with id " + credentials.get('id') + " doesn't exist."
            if not check_password_hash(existing_user.password, credentials.get('old_password')):
                valid = False
                msg = "Current password is not correct."

        if valid:
            valid, msg = UserValidator.validate_password(credentials.get('new_password'))

        return valid, msg
