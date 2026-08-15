<template>
  <section class="section">
    <div class="section-head" v-reveal>
      <span class="eyebrow">Os Mensageiros Celestes</span>
      <h2>Anjos e Arcanjos</h2>
      <p>
        Clique em um anjo para conhecer sua história, missão e lugar na tradição
        católica.
      </p>
    </div>

    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="card-grid">
      <router-link
        v-for="angel in angels"
        :key="angel.id"
        :to="{ name: 'angel-detail', params: { id: angel.id } }"
        class="card angel-card"
        v-reveal
      >
        <div class="icon" v-html="iconMap[angel.icon]"></div>
        <span class="tag">{{ angel.title }}</span>
        <h3>{{ angel.name }}</h3>
        <p>{{ angel.short_text }}</p>
        <span class="card-link">Ler mais →</span>
      </router-link>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { iconMap } from "../utils/iconMap";

const angels = ref([]);
const loading = ref(true);
const error = ref("");

async function fetchAngels() {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/angels");
    angels.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar os anjos.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchAngels);
</script>
