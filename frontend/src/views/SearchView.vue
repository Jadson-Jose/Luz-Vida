<template>
  <section class="search-view">
    <div class="section-head" v-reveal>
      <span class="eyebrow">Busca na Bíblia</span>
      <h2>Resultados para "{{ query }}"</h2>
      <p v-if="total > 0">{{ total }} versículo(s) encontrado(s)</p>
    </div>

    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else-if="results.length" class="results-list">
      <article
        v-for="result in results"
        :key="result.verse.id"
        class="result-item"
        v-reveal
      >
        <p class="verse-text">{{ result.verse.text }}</p>
        <p class="verse-ref">
          {{ result.book_name }} {{ result.chapter_number }},
          {{ result.verse.number }}
        </p>
        <router-link
          :to="{ name: 'chapter', params: { id: result.verse.chapter_id } }"
          class="btn-link"
        >
          Ler capítulo →
        </router-link>
      </article>
    </div>

    <p v-else class="no-results">Nenhum versículo encontrado.</p>
  </section>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const query = ref(route.query.q || "");
const results = ref([]);
const loading = ref(false);
const error = ref("");
const total = ref(0);

async function performSearch() {
  if (!query.value.trim()) return;
  loading.value = true;
  error.value = "";
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/search", {
      params: { q: query.value },
    });
    results.value = response.data;
    total.value = response.data.length;
  } catch (err) {
    error.value = "Erro ao buscar versículos.";
    console.error(err);
  } finally {
    loading.value = false;
  }
}

// Observa mudanças no parâmetro q da URL
watch(
  () => route.query.q,
  (newQ) => {
    query.value = newQ || "";
    performSearch();
  },
  { immediate: true },
);

onMounted(() => {
  console.log("SearchView montado");
});
</script>

<style scoped>
.search-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
}
.results-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 2rem;
}
.result-item {
  background: var(--parchment-deep);
  border: 1px solid var(--parchment-line);
  border-radius: 6px;
  padding: 1.25rem;
  transition:
    box-shadow 0.2s,
    border-color 0.2s;
}
.result-item:hover {
  box-shadow: var(--shadow);
  border-color: var(--gold);
}
.verse-text {
  font-family: "Cormorant Garamond", serif;
  font-size: 1.2rem;
  font-style: italic;
  color: var(--blue-deep);
}
.verse-ref {
  font-family: "Cinzel", serif;
  font-size: 0.8rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--wine);
  margin: 0.5rem 0;
}
.btn-link {
  background: none;
  border: none;
  color: var(--blue);
  cursor: pointer;
  font-family: "Cinzel", serif;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  text-decoration: none;
}
.btn-link:hover {
  text-decoration: underline;
}
.loading,
.error,
.no-results {
  text-align: center;
  font-style: italic;
  color: var(--ink-soft);
  margin-top: 2rem;
}
</style>
