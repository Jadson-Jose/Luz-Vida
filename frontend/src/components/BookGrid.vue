<template>
  <div class="book-grid">
    <p v-if="loading" class="loading">Carregando livros…</p>
    <p v-if="error" class="error">{{ error }}</p>

    <router-link
      v-for="book in books"
      :key="book.id"
      :to="{ name: 'book-chapters', params: { id: book.id } }"
      class="card book-card"
    >
      <span class="tag">{{ book.abbreviation }}</span>
      <h3>{{ book.name }}</h3>
      <p>
        {{ book.chapters ? book.chapters.length + " capítulos" : "Leia agora" }}
      </p>
    </router-link>
  </div>
</template>

<script setup>
defineProps({
  books: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
  error: {
    type: String,
    default: "",
  },
});
</script>
