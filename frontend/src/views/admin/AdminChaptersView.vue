<template>
  <div class="admin-chapters">
    <div class="admin-header">
      <router-link to="/admin/livros" class="back-link"
        >← Voltar aos livros</router-link
      >
      <h1>Capítulos do Livro #{{ bookId }}</h1>
      <button class="btn btn-primary" @click="openCreateForm">
        Novo Capítulo
      </button>
    </div>

    <div v-if="showForm" class="form-card" v-reveal>
      <h2>{{ editingChapter ? "Editar Capítulo" : "Novo Capítulo" }}</h2>
      <form @submit.prevent="saveChapter">
        <div class="form-group">
          <label for="number">Número</label>
          <input id="number" type="number" v-model="form.number" required />
        </div>
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Salvar</button>
          <button type="button" class="btn btn-ghost" @click="closeForm">
            Cancelar
          </button>
        </div>
      </form>
    </div>

    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <template v-else>
      <table class="admin-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Número</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="chapter in chapters" :key="chapter.id">
            <td>{{ chapter.id }}</td>
            <td>{{ chapter.number }}</td>
            <td>
              <button class="btn-link" @click="editChapter(chapter)">
                Editar
              </button>
              <button
                class="btn-link danger"
                @click="deleteChapter(chapter.id)"
              >
                Excluir
              </button>
              <router-link
                :to="{
                  name: 'admin-verses',
                  params: { chapterId: chapter.id },
                }"
                class="btn-link"
                >Versículos</router-link
              >
            </td>
          </tr>
        </tbody>
      </table>

      <PaginationBar
        :current-page="currentPage"
        :total-pages="totalPages"
        @change-page="changePage"
      />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
import api from "../../api/client";
import PaginationBar from "../../components/PaginationBar.vue";

const route = useRoute();
const bookId = route.params.bookId;

const chapters = ref([]);
const loading = ref(true);
const error = ref("");
const showForm = ref(false);
const editingChapter = ref(null);
const form = ref({ number: 1 });

// Paginação
const currentPage = ref(1);
const pageSize = 10;
const totalItems = ref(0);
const totalPages = computed(() => Math.ceil(totalItems.value / pageSize));

async function fetchChapters() {
  loading.value = true;
  error.value = "";
  try {
    const response = await api.get(`/books/${bookId}/chapters`, {
      params: {
        skip: (currentPage.value - 1) * pageSize,
        limit: pageSize,
      },
    });
    chapters.value = response.data;
    totalItems.value = parseInt(response.headers["x-total-count"] || "0");
  } catch (err) {
    error.value = "Erro ao carregar capítulos.";
  } finally {
    loading.value = false;
  }
}

function changePage(page) {
  currentPage.value = page;
  fetchChapters();
}

function openCreateForm() {
  editingChapter.value = null;
  form.value = { number: 1 };
  showForm.value = true;
}

function editChapter(chapter) {
  editingChapter.value = chapter;
  form.value = { number: chapter.number };
  showForm.value = true;
}

function closeForm() {
  showForm.value = false;
  editingChapter.value = null;
  form.value = { number: 1 };
}

async function saveChapter() {
  try {
    if (editingChapter.value) {
      await api.put(`/chapters/${editingChapter.value.id}`, {
        ...form.value,
        book_id: parseInt(bookId),
      });
    } else {
      await api.post("/chapters", { ...form.value, book_id: parseInt(bookId) });
    }
    closeForm();
    fetchChapters();
  } catch (err) {
    alert("Erro ao salvar capítulo.");
  }
}

async function deleteChapter(id) {
  if (!confirm("Excluir este capítulo e todos os seus versículos?")) return;
  try {
    await api.delete(`/chapters/${id}`);
    fetchChapters();
  } catch (err) {
    alert("Erro ao excluir capítulo.");
  }
}

onMounted(fetchChapters);
</script>

<style scoped>
.admin-chapters {
  max-width: 800px;
}
.admin-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}
.back-link {
  font-family: "Cinzel", serif;
  font-size: 0.8rem;
  text-transform: uppercase;
  color: var(--wine);
  text-decoration: none;
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
