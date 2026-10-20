<template>
  <section class="section">
    <div class="section-head reveal">
      <span class="eyebrow">Capítulos</span>
      <h2>{{ bookName }}</h2>
    </div>
    <div v-if="loading" class="loading">Carregando...</div>
    <div v-else class="chapter-list">
      <router-link
        v-for="chapter in chapters"
        :key="chapter.id"
        :to="{ name: 'chapter', params: { id: chapter.id } }"
        class="card chapter-card"
      >
        <span class="tag">Capítulo</span>
        <h3>{{ chapter.number }}</h3>
      </router-link>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import api from "../api/client"; // <-- Importando a instância correta

const route = useRoute();
const chapters = ref([]);
const bookName = ref("");
const loading = ref(true);

async function fetchBook() {
  try {
    // CORREÇÃO AQUI: usa 'api' e template string normal
    const response = await api.get(`books/${route.params.id}`);
    bookName.value = response.data.name;
    chapters.value = response.data.chapters;
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(fetchBook);
</script>