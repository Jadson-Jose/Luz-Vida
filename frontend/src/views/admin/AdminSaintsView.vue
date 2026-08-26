<template>
  <div class="admin-saints">
    <div class="admin-header">
      <h1>Gerenciar Santos</h1>
      <button class="btn btn-primary" @click="openCreateForm">
        Novo Santo
      </button>
    </div>

    <!-- Formulário de criação/edição -->
    <div v-if="showForm" class="form-card" v-reveal>
      <h2>{{ editingSaint ? "Editar Santo" : "Novo Santo" }}</h2>
      <form @submit.prevent="saveSaint">
        <div class="form-group">
          <label for="name">Nome</label>
          <input id="name" v-model="form.name" required />
        </div>
        <div class="form-group">
          <label for="title">Título</label>
          <input id="title" v-model="form.title" />
        </div>
        <div class="form-group">
          <label for="feast_day">Dia de Festa</label>
          <input
            id="feast_day"
            v-model="form.feast_day"
            placeholder="Ex.: 4 de outubro"
          />
        </div>
        <div class="form-group">
          <label for="image_url">URL da Imagem</label>
          <input
            id="image_url"
            v-model="form.image_url"
            placeholder="https://..."
          />
        </div>
        <div class="form-group">
          <label for="short_text">Texto Curto</label>
          <textarea
            id="short_text"
            v-model="form.short_text"
            rows="2"
            required
          ></textarea>
        </div>
        <div class="form-group">
          <label for="full_text">Texto Completo</label>
          <textarea
            id="full_text"
            v-model="form.full_text"
            rows="5"
            required
          ></textarea>
        </div>
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Salvar</button>
          <button type="button" class="btn btn-ghost" @click="closeForm">
            Cancelar
          </button>
        </div>
      </form>
    </div>

    <!-- Lista de santos -->
    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <table v-else class="admin-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Título</th>
          <th>Festa</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="saint in saints" :key="saint.id">
          <td>{{ saint.id }}</td>
          <td>{{ saint.name }}</td>
          <td>{{ saint.title }}</td>
          <td>{{ saint.feast_day }}</td>
          <td>
            <button class="btn-link" @click="editSaint(saint)">Editar</button>
            <button class="btn-link danger" @click="deleteSaint(saint.id)">
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
import api from "../../api/client";

const saints = ref([]);
const loading = ref(true);
const error = ref("");
const showForm = ref(false);
const editingSaint = ref(null);
const form = ref({
  name: "",
  title: "",
  feast_day: "",
  image_url: "",
  short_text: "",
  full_text: "",
});

async function fetchSaints() {
  loading.value = true;
  error.value = "";
  try {
    const response = await api.get("/saints");
    saints.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar santos.";
  } finally {
    loading.value = false;
  }
}

function openCreateForm() {
  editingSaint.value = null;
  form.value = {
    name: "",
    title: "",
    feast_day: "",
    image_url: "",
    short_text: "",
    full_text: "",
  };
  showForm.value = true;
}

function editSaint(saint) {
  editingSaint.value = saint;
  form.value = {
    name: saint.name,
    title: saint.title || "",
    feast_day: saint.feast_day || "",
    image_url: saint.image_url || "",
    short_text: saint.short_text,
    full_text: saint.full_text,
  };
  showForm.value = true;
}

function closeForm() {
  showForm.value = false;
  editingSaint.value = null;
  form.value = {
    name: "",
    title: "",
    feast_day: "",
    image_url: "",
    short_text: "",
    full_text: "",
  };
}

async function saveSaint() {
  try {
    if (editingSaint.value) {
      await api.put(`/saints/${editingSaint.value.id}`, form.value);
    } else {
      await api.post("/saints", form.value);
    }
    closeForm();
    fetchSaints();
  } catch (err) {
    alert("Erro ao salvar santo.");
  }
}

async function deleteSaint(id) {
  if (!confirm("Tem certeza que deseja excluir este santo?")) return;
  try {
    await api.delete(`/saints/${id}`);
    fetchSaints();
  } catch (err) {
    alert("Erro ao excluir santo.");
  }
}

onMounted(fetchSaints);
</script>

<style scoped>
.admin-saints {
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
</style>
