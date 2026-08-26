<template>
  <section class="section saint-detail">
    <div v-if="loading" class="loading">Carregando…</div>

    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else-if="saint" class="detail-content">
      <router-link to="/santos" class="back-link"
        >← Voltar aos santos</router-link
      >

      <div class="detail-header" v-reveal>
        <div class="saint-image-large">
          <img
            v-if="saint.image_url"
            :src="saint.image_url"
            :alt="saint.name"
          />
          <div v-else class="placeholder">✠</div>
        </div>
        <div>
          <span class="eyebrow">{{ saint.title || "Santo" }}</span>
          <h1>{{ saint.name }}</h1>
          <p v-if="saint.feast_day" class="feast">
            <em>Festa: {{ saint.feast_day }}</em>
          </p>
        </div>
      </div>

      <div class="gold-rule"></div>

      <div class="detail-text" v-reveal>
        <p class="short-text">{{ saint.short_text }}</p>
        <p>{{ saint.full_text }}</p>
      </div>
    </div>

    <div v-else class="loading">Santo não encontrado.</div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const saint = ref(null);
const loading = ref(true);
const error = ref("");

async function fetchSaint() {
  loading.value = true;
  error.value = "";
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/saints/${route.params.id}`,
    );
    saint.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar o santo.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchSaint);
</script>

<style scoped>
.detail-header {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}
.saint-image-large {
  width: 100px;
  height: 100px;
  flex-shrink: 0;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--parchment-line);
}
.saint-image-large img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.placeholder {
  font-size: 2.5rem;
  color: var(--wine);
}
.feast {
  color: var(--ink-soft);
  font-style: italic;
}
.detail-text {
  max-width: 700px;
  font-size: 1.1rem;
  line-height: 1.7;
}
.short-text {
  font-style: italic;
  color: var(--ink-soft);
  margin-bottom: 20px;
}
.back-link {
  display: inline-block;
  margin-bottom: 30px;
  color: var(--wine);
  font-family: "Cinzel", serif;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
}
.back-link:hover {
  text-decoration: underline;
}
</style>
