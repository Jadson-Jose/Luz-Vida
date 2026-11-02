<template>
  <div class="admin-church">
    <div class="admin-header">
      <h1>Conhecendo a Igreja</h1>
      <button class="btn btn-primary" @click="openCreateForm">Novo Artigo</button>
    </div>

    <!-- Formulário -->
    <div v-if="showForm" class="form-card" v-reveal>
      <h2>{{ editingItem ? 'Editar Artigo' : 'Novo Artigo' }}</h2>
      <form @submit.prevent="saveItem">
        <div class="form-row">
          <div class="form-group">
            <label for="category">Categoria</label>
            <select id="category" v-model="form.category" required>
              <option value="historia">História da Igreja</option>
              <option value="catecismo">Catecismo</option>
              <option value="documentos">Documentos Papais</option>
              <option value="oracoes">Orações e Terço</option>
            </select>
          </div>
          <div class="form-group">
            <label for="order">Ordem de Exibição</label>
            <input id="order" type="number" v-model="form.order" required />
          </div>
        </div>
        <div class="form-group">
          <label for="title">Título do Artigo</label>
          <input id="title" v-model="form.title" required placeholder="Ex: A Igreja Primitiva" />
        </div>
        <div class="form-group">
          <label for="content">Conteúdo (Pode usar Enter para parágrafos)</label>
          <textarea id="content" v-model="form.content" rows="15" required></textarea>
        </div>
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Salvar</button>
          <button type="button" class="btn btn-ghost" @click="closeForm">Cancelar</button>
        </div>
      </form>
    </div>

    <!-- Lista -->
    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <table v-else class="admin-table">
      <thead>
        <tr>
          <th>Ordem</th>
          <th>Categoria</th>
          <th>Título</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.order }}</td>
          <td>{{ translateCategory(item.category) }}</td>
          <td>{{ item.title }}</td>
          <td>
            <button class="btn-link" @click="editItem(item)">Editar</button>
            <button class="btn-link danger" @click="deleteItem(item.id)">Excluir</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../../api/client'

const items = ref([])
const loading = ref(true)
const error = ref('')
const showForm = ref(false)
const editingItem = ref(null)

const form = ref({
  category: 'historia',
  title: '',
  content: '',
  order: 1
})

const translateCategory = (cat) => {
  const map = { historia: 'História', catecismo: 'Catecismo', documentos: 'Documentos', oracoes: 'Orações' }
  return map[cat] || cat
}

async function fetchItems() {
  loading.value = true
  try {
    // Busca os itens de todas as categorias (criamos uma rota rápida no backend para isso, ou buscamos uma por uma)
    // Para simplificar, vamos buscar todas as categorias em paralelo
    const [hist, cat, doc, ora] = await Promise.all([
      api.get('church/historia'),
      api.get('church/catecismo'),
      api.get('church/documentos'),
      api.get('church/oracoes')
    ])
    items.value = [...hist.data, ...cat.data, ...doc.data, ...ora.data].sort((a, b) => a.order - b.order)
  } catch (err) {
    error.value = 'Erro ao carregar os artigos.'
  } finally {
    loading.value = false
  }
}

function openCreateForm() {
  editingItem.value = null
  form.value = { category: 'historia', title: '', content: '', order: 1 }
  showForm.value = true
}

function editItem(item) {
  editingItem.value = item
  form.value = { category: item.category, title: item.title, content: item.content, order: item.order }
  showForm.value = true
}

function closeForm() {
  showForm.value = false
  editingItem.value = null
}

async function saveItem() {
  try {
    if (editingItem.value) {
      await api.put(`church/${editingItem.value.id}`, form.value)
    } else {
      await api.post('church/', form.value)
    }
    closeForm()
    fetchItems()
  } catch (err) {
    alert('Erro ao salvar o artigo.')
  }
}

async function deleteItem(id) {
  if (!confirm('Tem certeza que deseja excluir este artigo?')) return
  try {
    await api.delete(`church/${id}`)
    fetchItems()
  } catch (err) {
    alert('Erro ao excluir o artigo.')
  }
}

onMounted(fetchItems)
</script>

<style scoped>
.admin-church { max-width: 1000px; }
.admin-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }
.form-card { background: var(--parchment-deep); border: 1px solid var(--parchment-line); padding: 1.5rem; margin-bottom: 2rem; border-radius: 6px; }
.form-row { display: flex; gap: 1rem; }
.form-row .form-group { flex: 1; }
.form-group { margin-bottom: 1rem; }
.form-group label { display: block; font-family: "Cinzel", serif; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--blue-deep); margin-bottom: 0.25rem; }
.form-group input, .form-group select, .form-group textarea { width: 100%; padding: 0.6rem 0.8rem; border: 1px solid var(--parchment-line); border-radius: 4px; background: var(--parchment); font-size: 1rem; font-family: "EB Garamond", serif; }
.form-group textarea { resize: vertical; }
.form-actions { display: flex; gap: 1rem; margin-top: 1.5rem; }
.admin-table { width: 100%; border-collapse: collapse; background: var(--parchment); border: 1px solid var(--parchment-line); }
.admin-table th, .admin-table td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid var(--parchment-line); }
.admin-table th { background: var(--parchment-deep); font-family: "Cinzel", serif; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; }
.btn-link { background: none; border: none; color: var(--blue); cursor: pointer; margin-right: 0.75rem; font-family: "Cinzel", serif; font-size: 0.75rem; text-transform: uppercase; }
.btn-link.danger { color: var(--wine); }
</style>