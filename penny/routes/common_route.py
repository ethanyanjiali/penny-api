from flask import current_app, Blueprint, request


common = Blueprint('common', __name__, url_prefix='/common')


@common.route('/feedback', methods=['POST'])
def create_event():
    from ..mediators.common.submit_feedback_mediator import SubmitFeedbackMediator
    mediator = SubmitFeedbackMediator(request)
    response = mediator.run()
    return response


@common.route('/lang', methods=['GET'])
def get_languages():
    return request.headers['Accept-Language']
