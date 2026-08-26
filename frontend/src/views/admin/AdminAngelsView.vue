<template>
  <div class="admin-angels">
    <div class="admin-header">
      <h1>Gerenciar Anjos</h1>
      <button class="btn btn-primary" @click="openCreateForm">Novo Anjo</button>
    </div>

    <!-- Formulário de criação/edição -->
    <div v-if="showForm" class="form-card" v-reveal>
      <h2>{{ editingAngel ? "Editar Anjo" : "Novo Anjo" }}</h2>
      <form @submit.prevent="saveAngel">
        <div class="form-group">
          <label for="name">Nome</label>
          <input id="name" v-model="form.name" required />
        </div>
        <div class="form-group">
          <label for="title">Título</label>
          <input id="title" v-model="form.title" required />
        </div>
        <div class="form-group">
          <label for="icon">Ícone</label>
          <select id="icon" v-model="form.icon" required>
            <option disabled value="">Selecione um ícone</option>
            <option v-for="(svg, key) in iconMap" :key="key" :value="key">
              {{ key }}
            </option>
          </select>
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

    <!-- Lista de anjos -->
    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <table v-else class="admin-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Título</th>
          <th>Ícone</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="angel in angels" :key="angel.id">
          <td>{{ angel.id }}</td>
          <td>{{ angel.name }}</td>
          <td>{{ angel.title }}</td>
          <td>
            <span v-html="iconMap[angel.icon]" class="table-icon"></span>
          </td>
          <td>
            <button class="btn-link" @click="editAngel(angel)">Editar</button>
            <button class="btn-link danger" @click="deleteAngel(angel.id)">
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
import { iconMap } from "../../utils/iconMap";

const angels = ref([]);
const loading = ref(true);
const error = ref("");
const showForm = ref(false);
const editingAngel = ref(null);
const form = ref({
  name: "",
  title: "",
  icon: "",
  short_text: "",
  full_text: "",
});

async function fetchAngels() {
  loading.value = true;
  error.value = "";
  try {
    const response = await api.get("/angels");
    angels.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar anjos.";
  } finally {
    loading.value = false;
  }
}

function openCreateForm() {
  editingAngel.value = null;
  form.value = {
    name: "",
    title: "",
    icon: "",
    short_text: "",
    full_text: "",
  };
  showForm.value = true;
}

function editAngel(angel) {
  editingAngel.value = angel;
  form.value = {
    name: angel.name,
    title: angel.title,
    icon: angel.icon,
    short_text: angel.short_text,
    full_text: angel.full_text,
  };
  showForm.value = true;
}

function closeForm() {
  showForm.value = false;
  editingAngel.value = null;
  form.value = {
    name: "",
    title: "",
    icon: "",
    short_text: "",
    full_text: "",
  };
}

async function saveAngel() {
  try {
    if (editingAngel.value) {
      await api.put(`/angels/${editingAngel.value.id}`, form.value);
    } else {
      await api.post("/angels", form.value);
    }
    closeForm();
    fetchAngels();
  } catch (err) {
    alert("Erro ao salvar anjo.");
  }
}

async function deleteAngel(id) {
  if (!confirm("Tem certeza que deseja excluir este anjo?")) return;
  try {
    await api.delete(`/angels/${id}`);
    fetchAngels();
  } catch (err) {
    alert("Erro ao excluir anjo.");
  }
}

onMounted(fetchAngels);
</script>

<style scoped>
.admin-angels {
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
.form-group select,
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
.table-icon {
  display: inline-block;
  width: 30px;
  height: 30px;
  color: var(--wine);
}
.table-icon svg {
  width: 100%;
  height: 100%;
}
</style>
