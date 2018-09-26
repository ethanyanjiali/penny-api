from ..abstract_base_mediator import AbstractBaseMediator
from ...models.event import Event
from ...daos.event_dao import EventDAO
from flask import jsonify
import datetime
import uuid

class ReadEventMediator(AbstractBaseMediator):

    def __init__(self, event_id):
        self.event_id = event_id

    def run(self):
        if self.event_id is None:
            response = jsonify(message="Invalid request", success=False)
            response.status_code = 400
            return response

        event = EventDAO.read(self.event_id)

        if event is None:
            response = jsonify(message="Cannot find event", success=False)
            response.status_code = 400
            return response

        response = jsonify(event=event.to_dict(), success=True)
        response.status_code = 200
        return response
