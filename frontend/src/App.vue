<template>
  <AppHeader />
  <main>
    <router-view />
  </main>
  <AppFooter />
  <Analytics /> <!-- 2. Adicione o componente aqui -->
</template>

<script setup>
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";
import { Analytics } from "@vercel/analytics/vue"; // 1. Importe com o /vue no final
</script>