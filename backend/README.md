# Todo List Backend

A simple Flask-based REST API for the Todo List application.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `PUT /todos/<id>` - Update a todo
- `DELETE /todos/<id>` - Delete a todo

## Example Usage

### Create a todo
```bash
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries"}'
```

### Get all todos
```bash
curl http://localhost:5000/todos
```

### Update a todo
```bash
curl -X PUT http://localhost:5000/todos/<todo_id> \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

### Delete a todo
```bash
curl -X DELETE http://localhost:5000/todos/<todo_id>
``` 