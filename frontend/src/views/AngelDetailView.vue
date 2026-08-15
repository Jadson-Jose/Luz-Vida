<template>
  <section class="section angel-detail">
    <div v-if="loading" class="loading">Carregando…</div>

    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else-if="angel" class="detail-content">
      <router-link to="/anjos" class="back-link"
        >← Voltar aos anjos</router-link
      >

      <div class="detail-header" v-reveal>
        <div class="detail-icon" v-html="iconMap[angel.icon]"></div>
        <div>
          <span class="eyebrow">{{ angel.title }}</span>
          <h1>{{ angel.name }}</h1>
        </div>
      </div>

      <div class="gold-rule"></div>

      <div class="detail-text" v-reveal>
        <p class="short-text">{{ angel.short_text }}</p>
        <p>{{ angel.full_text }}</p>
      </div>
    </div>

    <div v-else class="loading">Anjo não encontrado.</div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { iconMap } from "../utils/iconMap";

const route = useRoute();
const angel = ref(null);
const loading = ref(true);
const error = ref("");

async function fetchAngel() {
  loading.value = true;
  error.value = "";
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/angels/${route.params.id}`,
    );
    angel.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar o anjo. Verifique se a API está rodando.";
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(fetchAngel);
</script>

<style scoped>
.detail-header {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 20px;
}
.detail-icon {
  width: 70px;
  height: 70px;
  color: var(--wine);
  flex-shrink: 0;
}
.detail-icon svg {
  width: 100%;
  height: 100%;
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
