# Todo Application

A simple Todo application built with Flask (backend) and Nuxt.js (frontend).

## Project Structure

```
.
├── backend/           # Flask backend
│   ├── app.py         # Main Flask application
│   ├── requirements.txt # Python dependencies
│   └── venv/          # Python virtual environment
├── frontend/          # Nuxt.js frontend
│   ├── components/    # Vue components
│   ├── pages/         # Nuxt pages
│   ├── nuxt.config.ts # Nuxt configuration
│   └── package.json   # Node.js dependencies
└── README.md          # This file
```

## Features

- Create, read, update, and delete todos
- Mark todos as completed
- Modern UI with Tailwind CSS
- RESTful API backend

## Backend (Flask)

The backend is a simple Flask application that provides a RESTful API for managing todos.

### API Endpoints

- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `PUT /todos/<todo_id>` - Update a todo
- `DELETE /todos/<todo_id>` - Delete a todo

### Running the Backend

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Activate the virtual environment:
   ```
   source venv/bin/activate  # On macOS/Linux
   # or
   .\venv\Scripts\activate  # On Windows
   ```

3. Install dependencies (if not already installed):
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

The backend will be available at http://localhost:5001.

## Frontend (Nuxt.js)

The frontend is built with Nuxt.js and uses Tailwind CSS for styling.

### Running the Frontend

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies (if not already installed):
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```

The frontend will be available at http://localhost:3001.

## Development

### Backend Development

The backend uses in-memory storage for todos, which is suitable for development. For a production environment, you would want to replace this with a database.

### Frontend Development

The frontend is configured to connect to the backend at http://localhost:5001. If you change the backend port, make sure to update the `apiBase` in `nuxt.config.ts`.

## Technologies Used

- **Backend**:
  - Flask
  - Flask-CORS
  - Python-dotenv

- **Frontend**:
  - Nuxt.js
  - Vue.js
  - Tailwind CSS
  - Axios

## Running the Project

To run the entire project, you can use the following one-liner commands:

### Backend
```bash
cd backend && source venv/bin/activate && python app.py
```

### Frontend
```bash
cd frontend && npm run dev
```
```

## License

This project is open source and available under the MIT License. 