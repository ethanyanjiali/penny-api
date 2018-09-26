from ..abstract_base_mediator import AbstractBaseMediator
from ...models.event import Event
from ...daos.event_dao import EventDAO
from flask import jsonify
import datetime
import uuid

class EditEventMediator(AbstractBaseMediator):

    def __init__(self, request, event_id):
        self.request = request
        self.event_id = event_id

    def run(self):
        payload = self.request.get_json()
        event_dict = payload['event']
        event = Event.from_dict(event_dict)

        if event.name is None or event.people is None or self.event_id is None:
            response = jsonify(message="Invalid request", success=False)
            response.status_code = 400
            return response

        existing_event = EventDAO.read(self.event_id)

        if event is None:
            response = jsonify(message="Cannot find event", success=False)
            response.status_code = 400
            return response
        
        existing_event.name = event.name
        existing_event.people = event.people

        updated_event = EventDAO.update(existing_event)
        response = jsonify(event=updated_event.to_dict(), success=True)
        response.status_code = 200
        return response
