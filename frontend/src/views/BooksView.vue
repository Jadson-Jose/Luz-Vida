<template>
  <section class="section">
    <div class="section-head reveal">
      <span class="eyebrow">Bíblia Sagrada</span>
      <h2>Livros</h2>
      <p v-if="searchQuery">Filtrando por "{{ searchQuery }}"</p>
    </div>
    <div v-if="loading" class="loading">Carregando...</div>
    <div v-else class="book-grid">
      <router-link
        v-for="book in filteredBooks"
        :key="book.id"
        :to="{ name: 'book-chapters', params: { id: book.id } }"
        class="card book-card"
      >
        <span class="tag">{{ book.abbreviation }}</span>
        <h3>{{ book.name }}</h3>
        <p>{{ book.chapters ? book.chapters.length + " capítulos" : "" }}</p>
      </router-link>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const books = ref([]);
const loading = ref(true);
const searchQuery = ref("");

// Observa o query param "search" vindo do header
watch(
  () => route.query.search,
  (newVal) => {
    searchQuery.value = newVal || "";
  },
  { immediate: true },
);

const filteredBooks = computed(() => {
  if (!searchQuery.value) return books.value;
  const q = searchQuery.value.toLowerCase();
  return books.value.filter((b) => b.name.toLowerCase().includes(q));
});

async function fetchBooks() {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/books");
    books.value = response.data;
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(fetchBooks);
</script>
