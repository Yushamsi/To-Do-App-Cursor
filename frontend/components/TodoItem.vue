<template>
  <div class="flex items-center justify-between p-4 bg-white rounded-lg shadow-sm mb-2 hover:shadow-md transition-shadow">
    <div class="flex items-center space-x-3">
      <input
        type="checkbox"
        :checked="todo.completed"
        @change="toggleComplete"
        class="w-5 h-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
      />
      <span :class="{ 'line-through text-gray-400': todo.completed }" class="text-gray-800">
        {{ todo.title }}
      </span>
    </div>
    <button
      @click="clickDelete"
      class="text-red-500 hover:text-red-700 focus:outline-none"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
    </button>
  </div>
</template>

<script setup lang="ts">
interface Todo {
  id: string;
  title: string;
  completed: boolean;
  created_at: string;
}

const props = defineProps<{
  todo: Todo;
}>();

const emit = defineEmits<{
  (e: 'update', id: string, completed: boolean): void;
  (e: 'delete', id: string): void;
}>();

const toggleComplete = () => {
  emit('update', props.todo.id, !props.todo.completed);
};

const clickDelete = () => {
  emit('delete', props.todo.id);
};
</script> 