<template>
  <section class="liturgy-section section" v-if="liturgy">
    <div class="liturgy-card" :style="{ borderTopColor: getColor(liturgy.liturgical_color) }">
      <div class="liturgy-header">
        <span class="eyebrow">Liturgia Diária</span>
        <h2>{{ formatDate(liturgy.date) }}</h2>
        <div class="liturgy-tags">
          <span class="tag">{{ liturgy.liturgical_season }}</span>
          <span class="tag" :style="{ backgroundColor: getColor(liturgy.liturgical_color), color: '#fff' }">
            {{ liturgy.liturgical_color }}
          </span>
        </div>
      </div>
      <div class="liturgy-content" v-if="liturgy.gospel">
        <h3>Evangelho do Dia</h3>
        <p class="gospel-text">{{ liturgy.gospel }}</p>
      </div>
      <router-link to="/liturgia" class="btn btn-ghost">Ler todas as leituras →</router-link>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/client'

const liturgy = ref(null)

const getColor = (color) => {
  const colors = {
    'Verde': '#2e7d32', 'Vermelho': '#c62828', 'Roxo': '#6a1b9a', 'Branco': '#9e9e9e', 'Rosa': '#e91e63'
  }
  return colors[color] || '#ccc'
}

const formatDate = (dateString) => {
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateString + 'T12:00:00').toLocaleDateString('pt-BR', options)
}

onMounted(async () => {
  try {
    const response = await api.get('liturgy/today')
    liturgy.value = response.data
  } catch (err) {
    console.error('Erro ao carregar a liturgia:', err)
  }
})
</script>

<style scoped>
.liturgy-section {
  max-width: 800px;
  margin: 0 auto;
  padding-top: 10px;
}
.liturgy-card {
  background: var(--parchment-deep);
  border: 1px solid var(--parchment-line);
  border-top: 5px solid #ccc;
  border-radius: 6px;
  padding: 2.5rem 2rem;
  text-align: center;
  box-shadow: var(--shadow);
}
.liturgy-header h2 {
  font-size: 1.8rem;
  margin: 10px 0;
  text-transform: capitalize;
  color: var(--blue-deep);
}
.liturgy-tags {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 2rem;
}
.tag {
  padding: 4px 12px;
  border-radius: 20px;
  font-family: 'Cinzel', serif;
  font-size: 0.75rem;
  background: #ddd;
  letter-spacing: 0.05em;
}
.liturgy-content {
  text-align: left;
  margin-bottom: 2rem;
  background: rgba(255,255,255,0.4);
  padding: 1.5rem;
  border-radius: 4px;
}
.liturgy-content h3 {
  font-family: 'Cinzel', serif;
  color: var(--wine);
  margin-bottom: 0.5rem;
  font-size: 1rem;
}
.gospel-text {
  font-family: 'EB Garamond', serif;
  font-size: 1.1rem;
  line-height: 1.6;
  white-space: pre-line;
  display: -webkit-box;
  -webkit-line-clamp: 6;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>