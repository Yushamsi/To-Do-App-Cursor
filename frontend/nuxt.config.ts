import { defineNuxtConfig } from 'nuxt/config';
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],

  runtimeConfig: {
    public: {
      apiBase: 'http://localhost:5001'
    }
  },

  devServer: {
    port: 3001
  },

  compatibilityDate: '2025-04-05'
})