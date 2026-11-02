<template>
  <section class="section church-view">
    <div class="header">
      <span class="eyebrow">Conhecendo a Igreja</span>
      <h1 class="capitalize">{{ currentCategoryName }}</h1>
    </div>

    <!-- Lista de tópicos da categoria -->
    <div v-if="!selectedTopic && topics.length > 0" class="topics-list">
      <router-link 
        v-for="topic in topics" 
        :key="topic.id" 
        :to="`/igreja/${category}/${topic.id}`"
        class="topic-card card"
      >
        <h3>{{ topic.title }}</h3>
        <span class="read-more">Ler artigo →</span>
      </router-link>
    </div>

    <!-- Leitura do tópico selecionado -->
    <div v-else-if="selectedTopic" class="topic-content">
      <router-link :to="`/igreja/${category}`" class="back-link">← Voltar para {{ currentCategoryName }}</router-link>
      <h2>{{ selectedTopic.title }}</h2>
      <div class="gold-rule"></div>
      <div class="text-content" v-html="formattedContent"></div>
    </div>

    <!-- Estado vazio -->
    <div v-else-if="!loading" class="empty">
      <p>Ainda não há conteúdo cadastrado nesta seção.</p>
    </div>
    
    <div v-if="loading" class="loading">Carregando...</div>
  </section>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '../api/client'

const route = useRoute()
const topics = ref([])
const selectedTopic = ref(null)
const loading = ref(true)

const category = computed(() => route.params.category || '')
const topicId = computed(() => route.params.id || null)

const currentCategoryName = computed(() => {
  const names = {
    'historia': 'História da Igreja',
    'catecismo': 'Catecismo',
    'documentos': 'Documentos Papais',
    'oracoes': 'Orações e Terço'
  }
  return names[category.value] || 'Conhecendo a Igreja'
})

// Transforma quebras de linha em parágrafos HTML
const formattedContent = computed(() => {
  if (!selectedTopic.value) return ''
  return selectedTopic.value.content
    .split('\n')
    .map(p => p.trim() ? `<p>${p}</p>` : '')
    .join('')
})

async function loadContent() {
  loading.value = true
  try {
    if (topicId.value) {
      const res = await api.get(`church/topic/${topicId.value}`)
      selectedTopic.value = res.data
      topics.value = [] 
    } else if (category.value) {
      const res = await api.get(`church/${category.value}`)
      topics.value = res.data
      selectedTopic.value = null
    }
  } catch (err) {
    console.error("Erro ao carregar conteúdo:", err)
  } finally {
    loading.value = false
  }
}

watch(() => route.fullPath, loadContent)
onMounted(loadContent)
</script>

<style scoped>
.church-view { max-width: 900px; margin: 0 auto; }
.header { text-align: center; margin-bottom: 3rem; }
.header h1 { font-size: 2.5rem; text-transform: capitalize; }
.capitalize { text-transform: capitalize; }

.topics-list { display: grid; gap: 1rem; }
.topic-card { 
  text-decoration: none; 
  color: var(--ink); 
  display: flex; 
  justify-content: space-between; 
  align-items: center;
  padding: 1.5rem 2rem;
}
.topic-card h3 { margin: 0; font-size: 1.4rem; }
.topic-card:hover h3 { color: var(--wine); }
.read-more {
  font-family: 'Cinzel', serif;
  font-size: 0.8rem;
  color: var(--wine);
}

.topic-content { max-width: 750px; margin: 0 auto; }
.topic-content h2 { font-size: 2.2rem; text-align: center; margin-bottom: 1rem; }
.text-content { 
  font-family: 'EB Garamond', serif; 
  font-size: 1.2rem; 
  line-height: 1.8; 
  color: var(--ink);
}
.text-content :deep(p) { margin-bottom: 1.5rem; }

.empty, .loading { text-align: center; font-style: italic; color: var(--ink-soft); margin-top: 2rem; }
</style>