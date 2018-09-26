from ..abstract_base_mediator import AbstractBaseMediator
from ...models.event import Event
from ...models.expense import Expense
from ...daos.event_dao import EventDAO
from flask import jsonify
import datetime
import uuid

class DeleteExpenseMediator(AbstractBaseMediator):

    def __init__(self, event_id, expense_id):
        self.event_id = event_id
        self.expense_id = expense_id

    def run(self):
        if self.event_id is None or self.expense_id is None:
            response = jsonify(message="Invalid request", success=False)
            response.status_code = 400
            return response

        event = EventDAO.read(self.event_id)

        if event is None:
            response = jsonify(message="Cannot find event", success=False)
            response.status_code = 400
            return response

        new_expenses = []
        if event.expenses != None:
            new_expenses = event.expenses

        index = 0

        for expense in new_expenses:
            if expense['id'] == self.expense_id:
                del new_expenses[index]
            index = index + 1

        event.expenses = new_expenses

        updated_event = EventDAO.update(event)
        response = jsonify(event=updated_event.to_dict(), success=True)
        response.status_code = 200
        return response
