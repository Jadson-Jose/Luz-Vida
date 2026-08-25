<template>
  <div class="admin-verses">
    <div class="admin-header">
      <router-link
        v-if="bookId"
        :to="{ name: 'admin-chapters', params: { bookId: bookId } }"
        class="back-link"
        >← Voltar aos capítulos</router-link
      >
      <h1>Versículos do Capítulo #{{ chapterId }}</h1>
      <button class="btn btn-primary" @click="openCreateForm">
        Novo Versículo
      </button>
    </div>

    <div v-if="showForm" class="form-card" v-reveal>
      <h2>{{ editingVerse ? "Editar Versículo" : "Novo Versículo" }}</h2>
      <form @submit.prevent="saveVerse">
        <div class="form-group">
          <label for="number">Número</label>
          <input id="number" type="number" v-model="form.number" required />
        </div>
        <div class="form-group">
          <label for="text">Texto</label>
          <textarea id="text" v-model="form.text" rows="4" required></textarea>
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
    <table v-else class="admin-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Número</th>
          <th>Texto</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="verse in verses" :key="verse.id">
          <td>{{ verse.id }}</td>
          <td>{{ verse.number }}</td>
          <td class="verse-text-preview">{{ verse.text }}</td>
          <td>
            <button class="btn-link" @click="editVerse(verse)">Editar</button>
            <button class="btn-link danger" @click="deleteVerse(verse.id)">
              Excluir
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import api from "../../api/client";

const route = useRoute();
const chapterId = route.params.chapterId;
const bookId = ref(null); // será obtido do capítulo
const verses = ref([]);
const loading = ref(true);
const error = ref("");
const showForm = ref(false);
const editingVerse = ref(null);
const form = ref({ number: 1, text: "" });

async function fetchVerses() {
  loading.value = true;
  try {
    const response = await api.get(`/chapters/${chapterId}`);
    verses.value = response.data.verses;
    bookId.value = response.data.book_id;
  } catch (err) {
    error.value = "Erro ao carregar versículos.";
  } finally {
    loading.value = false;
  }
}

function openCreateForm() {
  editingVerse.value = null;
  form.value = { number: 1, text: "" };
  showForm.value = true;
}

function editVerse(verse) {
  editingVerse.value = verse;
  form.value = { number: verse.number, text: verse.text };
  showForm.value = true;
}

function closeForm() {
  showForm.value = false;
  editingVerse.value = null;
  form.value = { number: 1, text: "" };
}

async function saveVerse() {
  try {
    if (editingVerse.value) {
      await api.put(`/verses/${editingVerse.value.id}`, {
        ...form.value,
        chapter_id: parseInt(chapterId),
      });
    } else {
      await api.post("/verses", {
        ...form.value,
        chapter_id: parseInt(chapterId),
      });
    }
    closeForm();
    fetchVerses();
  } catch (err) {
    alert("Erro ao salvar versículo.");
  }
}

async function deleteVerse(id) {
  if (!confirm("Excluir este versículo?")) return;
  try {
    await api.delete(`/verses/${id}`);
    fetchVerses();
  } catch (err) {
    alert("Erro ao excluir versículo.");
  }
}

onMounted(fetchVerses);
</script>

<style scoped>
.admin-verses {
  max-width: 900px;
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
.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.6rem 0.8rem;
  border: 1px solid var(--parchment-line);
  border-radius: 4px;
  background: var(--parchment);
  font-size: 1rem;
  font-family: "EB Garamond", serif;
}
.form-group textarea {
  resize: vertical;
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
.verse-text-preview {
  max-width: 400px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
