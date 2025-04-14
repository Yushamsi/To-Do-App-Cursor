from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for todos
todos = []

# Helper function to find a todo by id
def find_todo(todo_id):
    return next((todo for todo in todos if todo['id'] == todo_id), None)

@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todos"""
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    new_todo = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo"""
    todo = find_todo(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    data = request.get_json()
    
    if 'title' in data:
        todo['title'] = data['title']
    if 'completed' in data:
        todo['completed'] = data['completed']
    
    return jsonify(todo)

@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    todo = find_todo(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    todos.remove(todo)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5001) 