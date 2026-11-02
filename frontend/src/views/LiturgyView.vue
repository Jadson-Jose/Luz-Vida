<template>
  <section class="section liturgy-view" v-if="liturgy">
    <div class="header" :style="{ borderBottomColor: getColor(liturgy.liturgical_color) }">
      <span class="eyebrow">Liturgia Diária</span>
      <h1>{{ formatDate(liturgy.date) }}</h1>
      <div class="tags">
        <span class="tag">{{ liturgy.liturgical_season }}</span>
        <span class="tag" :style="{ backgroundColor: getColor(liturgy.liturgical_color), color: '#fff' }">
          {{ liturgy.liturgical_color }}
        </span>
      </div>
    </div>

    <div class="reading-block" v-if="liturgy.first_reading">
      <h2>Primeira Leitura</h2>
      <p>{{ liturgy.first_reading }}</p>
    </div>

    <div class="reading-block" v-if="liturgy.psalm">
      <h2>Salmo Responsorial</h2>
      <p>{{ liturgy.psalm }}</p>
    </div>

    <div class="reading-block" v-if="liturgy.second_reading">
      <h2>Segunda Leitura</h2>
      <p>{{ liturgy.second_reading }}</p>
    </div>

    <div class="reading-block highlight" v-if="liturgy.gospel">
      <h2>Evangelho</h2>
      <p>{{ liturgy.gospel }}</p>
    </div>
  </section>
  
  <section v-else-if="loading" class="section">
    <p class="loading">Carregando liturgia...</p>
  </section>
  <section v-else class="section">
    <p class="error">A liturgia de hoje ainda não está disponível.</p>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/client'

const liturgy = ref(null)
const loading = ref(true)

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
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.liturgy-view {
  max-width: 800px;
  margin: 0 auto;
}
.header {
  border-bottom: 4px solid #ccc;
  padding-bottom: 1.5rem;
  margin-bottom: 3rem;
  text-align: center;
}
.header h1 {
  font-size: 2.2rem;
  margin: 10px 0;
  text-transform: capitalize;
  color: var(--blue-deep);
}
.tags {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 15px;
}
.tag {
  padding: 6px 16px;
  border-radius: 20px;
  font-family: 'Cinzel', serif;
  font-size: 0.8rem;
  background: #ddd;
  letter-spacing: 0.05em;
}
.reading-block {
  margin-bottom: 3rem;
}
.reading-block h2 {
  font-family: 'Cinzel', serif;
  font-size: 1.3rem;
  color: var(--wine);
  margin-bottom: 1rem;
  border-bottom: 1px solid var(--parchment-line);
  padding-bottom: 5px;
}
.reading-block p {
  font-family: 'EB Garamond', serif;
  font-size: 1.2rem;
  line-height: 1.8;
  white-space: pre-line;
  color: var(--ink);
}
.highlight h2 {
  color: var(--blue-deep);
}
.loading, .error {
  text-align: center;
  font-style: italic;
  color: var(--ink-soft);
  margin-top: 3rem;
}
</style>