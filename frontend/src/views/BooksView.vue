<template>
  <div class="books-container">
    <h1>Livros da Bíblia</h1>
    <p v-if="loading">Carregando...</p>
    <p v-if="error" class="error">{{ error }}</p>
    <ul v-if="books.length" class="book-list">
      <li v-for="book in books" :key="book.id">
        <router-link :to="{ name: 'book-chapters', params: { id: book.id } }">
          <span class="book-name">{{ book.name }}</span>
          <span class="book-abbrev">{{ book.abbreviation }}</span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const books = ref([]);
const loading = ref(false);
const error = ref("");

// Função para buscar livros
async function fetchBooks() {
  loading.value = true;
  error.value = "";
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/books");
    books.value = response.data;
  } catch (err) {
    error.value =
      "Erro ao carregar os livros. Verifique se a API está rodando.";
  } finally {
    loading.value = false;
  }
}

// Executa quando o componente é montado
onMounted(fetchBooks);
</script>

<style scoped>
.books-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
}
.book-list {
  list-style: none;
  padding: 0;
}
.book-list li {
  margin-bottom: 0.5rem;
}
.book-list a {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 1rem;
  background-color: #f5f5f5;
  border-radius: 4px;
  text-decoration: none;
  color: #333;
}
.book-list a:hover {
  background-color: #e0e0e0;
}
.error {
  color: red;
}
</style>
