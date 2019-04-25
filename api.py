from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import datetime


app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'figure out how to do this', 'Created': '{}'.format(datetime.datetime.now()), 'Updated': '', 'Due_Date': 'yesterday', 'Completed': 'false'},
    'todo2': {'task': 'Do a task', 'Created': '{}'.format(datetime.datetime.now()), 'Updated': '', 'Due_Date': 'today', 'Completed': 'false'},
    'todo3': {'task': 'get groceries', 'Created': '{}'.format(datetime.datetime.now()), 'Updated': '', 'Due_Date': 'tomorrow', 'Completed': 'false'}
}


def todo_not_existent(todo_id):
    """Catch case for non existent todo items"""
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist. Try one of these {}!".format(
            todo_id, TODOS.keys()))


parser = reqparse.RequestParser()
parser.add_argument('task', help='Enter the name of your task')
parser.add_argument('Due_Date',
                    help='Confirm your due date')
parser.add_argument('Completed', type=bool, default=False)


class Todo(Resource):
    """View, delete, and update individual todo items"""

    def get(self, todo_id):
        todo_not_existent(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        todo_not_existent(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        completed_date = ''
        due_date = ''
        if args['Completed']:
            completed_date = str(datetime.datetime.now())
        if args['Due_Date']:
            due_date = args['Due_Date']
        else:
            due_date = TODOS[todo_id]['Due_Date']
        TODOS[todo_id] = {'task': args['task'], 'Created': TODOS[todo_id]['Created'], 'Updated': str(datetime.datetime.now(
        )), 'Due_Date': due_date, 'Completed': args['Completed'], 'Completion_Date': completed_date}
        return TODOS[todo_id], 201


class TodoList(Resource):
    """List of all todos and create new tasks auto-numbering the todo task"""

    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task'], 'Created': str(datetime.datetime.now(
        )), 'Due_Date': args['Due_Date'], 'Completed': args['Completed']}
        return TODOS[todo_id], 201


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
