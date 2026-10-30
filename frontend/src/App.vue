<template>
  <AppHeader />
  <main>
    <router-view />
  </main>
  <AppFooter />
  <Analytics mode="production" /> <!-- Adicione o componente aqui -->
</template>

<script setup>
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";
import { Analytics } from "@vercel/analytics/vue"; // Importe o componente específico para Vue
</script>