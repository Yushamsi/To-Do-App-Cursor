# Import necessary modules from Flask and Python's standard library
from flask import Flask, request, jsonify       # For building the API, handling requests, and returning JSON
from flask_cors import CORS                     # To allow cross-origin requests (important for frontend/backend communication)
import uuid                                     # To generate unique IDs for each todo
from datetime import datetime                   # To add timestamps when todos are created

# Initialise the Flask app
app = Flask(__name__)

# Enable CORS on the app (allows requests from other domains, useful when frontend is separate)
CORS(app)

# In-memory list to store todos (this will reset every time the server restarts)
todos = []

# Helper function to find a todo by its ID
def find_todo(todo_id):
    # Searches the list of todos for a todo with the matching 'id'
    # Returns the first match, or None if not found
    return next((todo for todo in todos if todo['id'] == todo_id), None)

# Route to get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    """Returns all the todos in the list"""
    return jsonify(todos)   # Convert the list of todos to JSON and return it

# Route to create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    """Creates a new todo item"""
    data = request.get_json()  # Get JSON data from the request body

    # Check if the data exists and has a 'title'
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400  # Return an error if no title is provided

    # Create a new todo dictionary
    new_todo = {
        'id': str(uuid.uuid4()),                   # Generate a unique ID as a string
        'title': data['title'],                    # Use the title from the user
        'completed': False,                        # Default status is not completed
        'created_at': datetime.now().isoformat()   # Record current time in ISO format
    }

    # Add the new todo to the list
    todos.append(new_todo)

    # Return the newly created todo with status 201 (created)
    return jsonify(new_todo), 201

# Route to update a specific todo by its ID
@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Updates an existing todo item"""
    todo = find_todo(todo_id)  # Try to find the todo with the given ID

    # If no todo found, return an error
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404

    data = request.get_json()  # Get updated data from the request body

    # If a new title is provided, update it
    if 'title' in data:
        todo['title'] = data['title']

    # If the completion status is provided, update it
    if 'completed' in data:
        todo['completed'] = data['completed']

    # Return the updated todo
    return jsonify(todo)

# Route to delete a specific todo by its ID
@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Deletes a todo item"""
    todo = find_todo(todo_id)  # Try to find the todo

    # If not found, return error
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404

    # Remove the todo from the list
    todos.remove(todo)

    # Return empty response with 204 (No Content)
    return '', 204

# Only run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Start the Flask server on port 5001 with debug mode on
