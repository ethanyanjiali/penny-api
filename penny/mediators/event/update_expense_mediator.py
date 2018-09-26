from ..abstract_base_mediator import AbstractBaseMediator
from ...models.event import Event
from ...models.expense import Expense
from ...daos.event_dao import EventDAO
from flask import jsonify
import datetime
import uuid

class UpdateExpenseMediator(AbstractBaseMediator):

    def __init__(self, request, event_id, index, expense_id):
        self.request = request
        self.event_id = event_id
        self.index = int(index)
        self.expense_id = expense_id

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def run(self):
        payload = self.request.get_json()
        expense_dict = payload['expense']

        if expense_dict.get('description') is None:
            response = jsonify(message="Please provide a description for this expense.", success=False)
            response.status_code = 400
            return response

        if expense_dict.get('involved') is None:
            response = jsonify(message="Please provide a involved people list for this expense.", success=False)
            response.status_code = 400
            return response

        if expense_dict.get('payor') is None:
            response = jsonify(message="Please provide a payor for this expense.", success=False)
            response.status_code = 400
            return response

        if expense_dict.get('amount') is None or not self.is_number(expense_dict.get('amount')):
            response = jsonify(message="Please provide a valid number for the money spent.", success=False)
            response.status_code = 400
            return response
        
        expenseType = expense_dict.get('type')
        if expenseType is not None:
            if expenseType == 'shares':
                shares = expense_dict.get('shares') 
                if shares is None:
                   response = jsonify(message="Please provide shares information if you want to split by shares.", success=False)
                   response.status_code = 400
                   return response
                for share in list(shares.values()):
                    try:
                        float(share)
                    except ValueError:
                        response = jsonify(message="The value of shares must be a number", success=False)
                        response.status_code = 400
                        return response
            if expenseType == 'percentage':
                percentage = expense_dict.get('percentage') 
                if percentage is None:
                   response = jsonify(message="Please provide percentage information if you want to split by percentage.", success=False)
                   response.status_code = 400
                   return response
                for percent in list(percentage.values()):
                    try:
                        float(percent)
                    except ValueError:
                        response = jsonify(message="The value of percentage must be a number", success=False)
                        response.status_code = 400
                        return response

        event = EventDAO.read(self.event_id)
        expense = Expense.from_dict(expense_dict)

        if event is None:
            response = jsonify(message="Cannot find event", success=False)
            response.status_code = 400
            return response

        new_expenses = []
        if event.expenses != None:
            new_expenses = event.expenses

        index = 0

        for existingExpense in new_expenses:
            if existingExpense['id'] == self.expense_id:
                break
            index = index + 1

        if index < 0 or index >= len(new_expenses):
            response = jsonify(message="The id of expense is not correct.", success=False)
            response.status_code = 400
            return response

        new_expenses[index] = expense.to_embedded()
        event.expenses = new_expenses

        updated_event = EventDAO.update(event)
        response = jsonify(event=updated_event.to_dict(), success=True)
        response.status_code = 200
        return response
