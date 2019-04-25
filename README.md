RESTful API using Flask that implements a TODO list

1. Support CRUD for TODO Items

2. TODO item contains:

   1. Title
   2. Creation date (auto-generated)
   3. Last updated date
   4. Due date
   5. Completed (true/false)
   6. Completion date

3. API endpoints:

   1. List all TODO items
   2. Retrieve a TODO item by Id
   3. Update TODO information: title, due date, and completed
   4. Delete a TODO item.

4. Stored in a simple 'dict' data structure

5. Handle custom exception when a TODO item is not found.

6. Unit tests for all api methods and responses

Example commands to use this app:

1. GET the list:
   curl http://localhost:5000/todos

2. GET a single task:
   curl http://localhost:5000/todos/todo3

3. DELETE a task:
   curl http://localhost:5000/todos/todo2 -X DELETE -v

4. Add a new task:
   curl http://localhost:5000/todos -d "task=something new" -X POST -v

5. Update a task:
   curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v
