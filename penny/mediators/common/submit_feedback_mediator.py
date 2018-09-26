from ..abstract_base_mediator import AbstractBaseMediator
from ...models.feedback import Feedback
from ...daos.feedback_dao import FeedbackDAO
from flask import jsonify
import datetime
import uuid
import re

class SubmitFeedbackMediator(AbstractBaseMediator):

    def __init__(self, request):
        self.request = request

    def run(self):
        payload = self.request.get_json()
        feedback_dict = payload['feedback']

        feedback = Feedback.from_dict(feedback_dict)

        if feedback.name is None:
            response = jsonify(message="Please provide your name.", success=False)
            response.status_code = 400
            return response

        if feedback.email is None or not re.match(r"[^@]+@[^@]+\.[^@]+", feedback.email):
            response = jsonify(message="Please provide a valid email.", success=False)
            response.status_code = 400
            return response

        if feedback.type is None:
            response = jsonify(message="Please select a type for your feedback.", success=False)
            response.status_code = 400
            return response

        if feedback.content is None:
            response = jsonify(message="Please write some description for your feedback.", success=False)
            response.status_code = 400
            return response

        feedback.id = str(uuid.uuid4())

        created_feedback = FeedbackDAO.create(feedback)
        response = jsonify(feedback=created_feedback.to_dict(), success=True)
        response.status_code = 200
        return response
