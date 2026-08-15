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
import axios from "axios";

const route = useRoute();
const chapters = ref([]);
const bookName = ref("");
const loading = ref(true);

async function fetchBook() {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/books/${route.params.id}`,
    );
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
