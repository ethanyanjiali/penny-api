from flask import current_app, Blueprint, request
from ..validators.user_validator import UserValidator
from flask_jwt import jwt_required, current_identity


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/create', methods=['POST'])
def create_user():
    from ..mediators.user.create_user_mediator import CreateUserMediator
    mediator = CreateUserMediator(request)
    response = mediator.run()
    return response


@user.route('/view', methods=['GET'])
@jwt_required()
def view_user():
    from ..mediators.user.view_user_mediator import ViewUserMediator
    mediator = ViewUserMediator(request, current_identity)
    response = mediator.run()
    return response


@user.route('/update', methods=['PUT'])
@jwt_required()
def update_user():
    from ..mediators.user.update_user_mediator import UpdateUserMediator
    mediator = UpdateUserMediator(request, current_identity)
    response = mediator.run()
    return response


@user.route('/password', methods=['PUT'])
def update_password():
    from ..mediators.user.update_password_mediator import UpdatePasswordMediator
    mediator = UpdatePasswordMediator(request, current_identity)
    response = mediator.run()
    return response


@user.route('/forget', methods=['POST'])
def forget_password():
    from ..mediators.user.create_reset_token_mediator import CreateResetTokenMediator
    mediator = CreateResetTokenMediator(request)
    response = mediator.run()
    return response
