<template>
  <div class="chapters-container">
    <h1>Capítulos de {{ bookName }}</h1>
    <p v-if="loading">Carregando...</p>
    <p v-if="error" class="error">{{ error }}</p>
    <ul v-if="chapters.length" class="chapter-list">
      <li v-for="chapter in chapters" :key="chapter.id">
        <router-link :to="{ name: 'chapter', params: { id: chapter.id } }">
          Capítulo {{ chapter.number }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const chapters = ref([]);
const bookName = ref("");
const loading = ref(false);
const error = ref("");

async function fetchBook() {
  loading.value = true;
  error.value = "";
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/books/${route.params.id}`,
    );
    bookName.value = response.data.name;
    chapters.value = response.data.chapters;
  } catch (err) {
    error.value = "Erro ao carregar os capítulos.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchBook);
</script>

<style scoped>
.chapters-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
}
.chapter-list {
  list-style: none;
  padding: 0;
}
.chapter-list li {
  margin-bottom: 0.5rem;
}
.chapter-list a {
  display: block;
  padding: 0.5rem 1rem;
  background-color: #f0f0f0;
  border-radius: 4px;
  text-decoration: none;
  color: #333;
}
.chapter-list a:hover {
  background-color: #ddd;
}
.error {
  color: red;
}
</style>
