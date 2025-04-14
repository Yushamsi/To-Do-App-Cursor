# Todo List Frontend

A modern Todo List application built with Nuxt 3 and Tailwind CSS.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Run the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Features

- Add new todos
- Mark todos as complete/incomplete
- Delete todos
- Responsive design
- Loading states and error handling

## Project Structure

- `components/` - Reusable Vue components
  - `AddTodo.vue` - Component for adding new todos
  - `TodoItem.vue` - Component for displaying individual todos
- `pages/` - Nuxt pages
  - `index.vue` - Main todo list page

## Development

- The application uses Nuxt 3 with the Composition API
- Styling is done with Tailwind CSS
- API communication is handled with Axios
- TypeScript is used for type safety

## Building for Production

```bash
npm run build
```

The built files will be in the `.output` directory. 