from ..abstract_base_mediator import AbstractBaseMediator
from ...models.event import Event
from ...daos.event_dao import EventDAO
from flask import jsonify
import datetime
import uuid

class CreateEventMediator(AbstractBaseMediator):

    def __init__(self, request):
        self.request = request

    def run(self):
        payload = self.request.get_json()
        event_dict = payload['event']

        event = Event.from_dict(event_dict)

        if event.name is None or event.people is None or len(event.people) is 0:
            response = jsonify(message="Invalid request", success=False)
            response.status_code = 400
            return response

        event.id = str(uuid.uuid4())

        created_event = EventDAO.create(event)
        response = jsonify(event=created_event.to_dict(), success=True)
        response.status_code = 200
        return response
