<template>
  <div class="admin-dashboard">
    <h1>Dashboard</h1>
    <p class="welcome">Visão geral do conteúdo da plataforma.</p>

    <div v-if="loading" class="loading">Carregando estatísticas…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="stats-grid">
      <router-link to="/admin/livros" class="stat-card">
        <span class="stat-value">{{ stats.books }}</span>
        <span class="stat-label">Livros</span>
      </router-link>
      <router-link to="/admin/livros" class="stat-card">
        <span class="stat-value">{{ stats.chapters }}</span>
        <span class="stat-label">Capítulos</span>
      </router-link>
      <router-link to="/admin/livros" class="stat-card">
        <span class="stat-value">{{ stats.verses }}</span>
        <span class="stat-label">Versículos</span>
      </router-link>
      <router-link to="/admin/anjos" class="stat-card">
        <span class="stat-value">{{ stats.angels }}</span>
        <span class="stat-label">Anjos</span>
      </router-link>
      <router-link to="/admin/santos" class="stat-card">
        <span class="stat-value">{{ stats.saints }}</span>
        <span class="stat-label">Santos</span>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../../api/client";

const stats = ref({
  books: 0,
  chapters: 0,
  verses: 0,
  angels: 0,
  saints: 0,
});
const loading = ref(true);
const error = ref("");

async function fetchStats() {
  loading.value = true;
  error.value = "";
  try {
    const response = await api.get("/stats");
    stats.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar estatísticas.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchStats);
</script>

<style scoped>
.admin-dashboard h1 {
  font-family: "Cormorant Garamond", serif;
  color: var(--blue-deep);
  margin-bottom: 0.5rem;
}
.welcome {
  color: var(--ink-soft);
  margin-bottom: 2rem;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
}
.stat-card {
  background: var(--parchment-deep);
  border: 1px solid var(--parchment-line);
  border-radius: 8px;
  padding: 1.5rem 1rem;
  text-align: center;
  text-decoration: none;
  color: var(--ink);
  transition:
    transform 0.2s,
    box-shadow 0.2s,
    border-color 0.2s;
}
.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow);
  border-color: var(--gold);
}
.stat-value {
  display: block;
  font-family: "Cinzel", serif;
  font-size: 2.5rem;
  font-weight: 600;
  color: var(--blue-deep);
  margin-bottom: 0.25rem;
}
.stat-label {
  font-family: "Cinzel", serif;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--wine);
}
.loading,
.error {
  text-align: center;
  font-style: italic;
  color: var(--ink-soft);
}
.error {
  color: var(--wine);
}
</style>
