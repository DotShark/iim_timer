<script setup lang="ts">
import { Timer } from "lucide-vue-next"
</script>

<template>
  <main class="bg-gradient-to-b from-gray-800 to-gray-900 text-white p-6">
    <div class="flex flex-col items-center justify-center min-h-screen gap-6">
      <Timer :size="128" color="#6ee7b7" />

      <h1 class="text-4xl font-title font-semibold text-center">Bienvenue sur IIM Timer</h1>

      <RouterLink to="/maps" class="text-white text-lg bg-emerald-700 hover:bg-emerald-800 focus:outline-none focus:ring-4 focus:ring-emerald-300 font-medium rounded-full px-5 py-2.5 text-center me-2 mb-2 dark:bg-emerald-600 dark:hover:bg-emerald-700 dark:focus:ring-emerald-800">
        Voir les maps
      </RouterLink>
    </div>
  </main>
</template>
