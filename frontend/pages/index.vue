<template>
  <div class="min-h-screen bg-gray-100 py-8">
    <div class="max-w-2xl mx-auto px-4">
      <h1 class="text-3xl font-bold text-gray-900 mb-8 text-center">Todo List</h1>
      
      <AddTodo @add="addTodo" />
      
      <div v-if="loading" class="text-center py-4">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-4 border-blue-500 border-t-transparent"></div>
      </div>
      
      <div v-else-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4">
        {{ error }}
      </div>
      
      <div v-else-if="todos.length === 0" class="text-center text-gray-500 py-8">
        No todos yet. Add one above!
      </div>
      
      <div v-else class="space-y-2">
        <TodoItem
          v-for="todo in todos"
          :key="todo.id"
          :todo="todo"
          @update="updateTodo"
          @delete="deleteTodo"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Todo {
  id: string;
  title: string;
  completed: boolean;
  created_at: string;
}

const config = useRuntimeConfig();
const apiBase = config.public.apiBase;

const todos = ref<Todo[]>([]);
const loading = ref(true);
const error = ref('');

// Fetch all todos
const fetchTodos = async () => {
  try {
    const response = await axios.get(`${apiBase}/todos`);
    todos.value = response.data;
  } catch (err) {
    error.value = 'Failed to load todos. Please try again later.';
    console.error('Error fetching todos:', err);
  } finally {
    loading.value = false;
  }
};

// Add a new todo
const addTodo = async (title: string) => {
  try {
    const response = await axios.post(`${apiBase}/todos`, { title });
    todos.value.unshift(response.data);
  } catch (err) {
    error.value = 'Failed to add todo. Please try again.';
    console.error('Error adding todo:', err);
  }
};

// Update a todo
const updateTodo = async (id: string, completed: boolean) => {
  try {
    const response = await axios.put(`${apiBase}/todos/${id}`, { completed });
    const index = todos.value.findIndex(todo => todo.id === id);
    if (index !== -1) {
      todos.value[index] = response.data;
    }
  } catch (err) {
    error.value = 'Failed to update todo. Please try again.';
    console.error('Error updating todo:', err);
  }
};

// Delete a todo
const deleteTodo = async (id: string) => {
  try {
    await axios.delete(`${apiBase}/todos/${id}`);
    todos.value = todos.value.filter(todo => todo.id !== id);
  } catch (err) {
    error.value = 'Failed to delete todo. Please try again.';
    console.error('Error deleting todo:', err);
  }
};

// Load todos when the component mounts
onMounted(fetchTodos);
</script> 