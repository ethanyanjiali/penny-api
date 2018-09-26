from flask import current_app, Blueprint, request


event = Blueprint('event', __name__, url_prefix='/event')


@event.route('/create', methods=['POST'])
def create_event():
    from ..mediators.event.create_event_mediator import CreateEventMediator
    mediator = CreateEventMediator(request)
    response = mediator.run()
    return response


@event.route('/edit/<event_id>/add-expense', methods=['POST'])
def add_expense(event_id):
    from ..mediators.event.add_expense_mediator import AddExpenseMediator
    mediator = AddExpenseMediator(request, event_id)
    response = mediator.run()
    return response


@event.route('/edit/<event_id>/<index>/update-expense/<expense_id>', methods=['PUT'])
def update_expense(event_id, index, expense_id):
    from ..mediators.event.update_expense_mediator import UpdateExpenseMediator
    mediator = UpdateExpenseMediator(request, event_id, index, expense_id)
    response = mediator.run()
    return response


@event.route('/<event_id>', methods=['GET'])
def read_event(event_id):
    from ..mediators.event.read_event_mediator import ReadEventMediator
    mediator = ReadEventMediator(event_id)
    response = mediator.run()
    return response


@event.route('/edit/<event_id>', methods=['POST'])
def update_event(event_id):
    from ..mediators.event.edit_event_mediator import EditEventMediator
    mediator = EditEventMediator(request, event_id)
    response = mediator.run()
    return response


@event.route('/delete/<event_id>/<expense_id>', methods=['POST'])
def delete_expense(event_id, expense_id):
    from ..mediators.event.delete_expense_mediator import DeleteExpenseMediator
    mediator = DeleteExpenseMediator(event_id, expense_id)
    response = mediator.run()
    return response
