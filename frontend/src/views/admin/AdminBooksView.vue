<template>
  <div class="admin-books">
    <div class="admin-header">
      <h1>Gerenciar Livros</h1>
      <button class="btn btn-primary" @click="openCreateForm">
        Novo Livro
      </button>
    </div>

    <!-- Formulário de criação/edição -->
    <div v-if="showForm" class="form-card" v-reveal>
      <h2>{{ editingBook ? "Editar Livro" : "Novo Livro" }}</h2>
      <form @submit.prevent="saveBook">
        <div class="form-group">
          <label for="name">Nome</label>
          <input id="name" v-model="form.name" required />
        </div>
        <div class="form-group">
          <label for="abbreviation">Abreviação</label>
          <input id="abbreviation" v-model="form.abbreviation" required />
        </div>
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Salvar</button>
          <button type="button" class="btn btn-ghost" @click="closeForm">
            Cancelar
          </button>
        </div>
      </form>
    </div>

    <!-- Lista de livros -->
    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <table v-else class="admin-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Abreviação</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.id }}</td>
          <td>{{ book.name }}</td>
          <td>{{ book.abbreviation }}</td>
          <td>
            <button class="btn-link" @click="editBook(book)">Editar</button>
            <button class="btn-link danger" @click="deleteBook(book.id)">
              Excluir
            </button>
            <router-link
              :to="{ name: 'admin-chapters', params: { bookId: book.id } }"
              class="btn-link"
            >
              Capítulos
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../../api/client";

const books = ref([]);
const loading = ref(true);
const error = ref("");
const showForm = ref(false);
const editingBook = ref(null);
const form = ref({
  name: "",
  abbreviation: "",
});

async function fetchBooks() {
  loading.value = true;
  error.value = "";
  try {
    const response = await api.get("/books");
    books.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar livros.";
  } finally {
    loading.value = false;
  }
}

function openCreateForm() {
  editingBook.value = null;
  form.value = { name: "", abbreviation: "" };
  showForm.value = true;
}

function editBook(book) {
  editingBook.value = book;
  form.value = { name: book.name, abbreviation: book.abbreviation };
  showForm.value = true;
}

function closeForm() {
  showForm.value = false;
  editingBook.value = null;
  form.value = { name: "", abbreviation: "" };
}

async function saveBook() {
  try {
    if (editingBook.value) {
      await api.put(`/books/${editingBook.value.id}`, form.value);
    } else {
      await api.post("/books", form.value);
    }
    closeForm();
    fetchBooks();
  } catch (err) {
    alert("Erro ao salvar o livro.");
  }
}

async function deleteBook(id) {
  if (!confirm("Tem certeza que deseja excluir este livro?")) return;
  try {
    await api.delete(`/books/${id}`);
    fetchBooks();
  } catch (err) {
    alert("Erro ao excluir o livro.");
  }
}

onMounted(fetchBooks);
</script>

<style scoped>
.admin-books {
  max-width: 900px;
}
.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}
.form-card {
  background: var(--parchment-deep);
  border: 1px solid var(--parchment-line);
  padding: 1.5rem;
  margin-bottom: 2rem;
  border-radius: 6px;
}
.form-group {
  margin-bottom: 1rem;
}
.form-group label {
  display: block;
  font-family: "Cinzel", serif;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--blue-deep);
  margin-bottom: 0.25rem;
}
.form-group input {
  width: 100%;
  padding: 0.6rem 0.8rem;
  border: 1px solid var(--parchment-line);
  border-radius: 4px;
  background: var(--parchment);
  font-size: 1rem;
}
.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}
.admin-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--parchment);
  border: 1px solid var(--parchment-line);
}
.admin-table th,
.admin-table td {
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 1px solid var(--parchment-line);
}
.admin-table th {
  background: var(--parchment-deep);
  font-family: "Cinzel", serif;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
.btn-link {
  background: none;
  border: none;
  color: var(--blue);
  cursor: pointer;
  margin-right: 0.75rem;
  font-family: "Cinzel", serif;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  text-decoration: none;
}
.btn-link.danger {
  color: var(--wine);
}
.btn-link:hover {
  text-decoration: underline;
}
</style>
