<template>
  <form @submit.prevent="addTodo" class="mb-6">
    <div class="flex gap-2">
      <input
        v-model="newTodo"
        type="text"
        placeholder="Add a new task..."
        class="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        :disabled="isLoading"
      />
      <button
        type="submit"
        class="px-4 py-2 text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
        :disabled="!newTodo.trim() || isLoading"
      >
        <span v-if="isLoading">Adding...</span>
        <span v-else>Add</span>
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const newTodo = ref('');
const isLoading = ref(false);

const emit = defineEmits<{
  (e: 'add', title: string): void;
}>();

const addTodo = async () => {
  if (!newTodo.value.trim()) return;
  
  isLoading.value = true;
  try {
    emit('add', newTodo.value.trim());
    newTodo.value = '';
  } finally {
    isLoading.value = false;
  }
};
</script> 