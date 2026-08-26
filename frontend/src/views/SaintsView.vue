<template>
  <section class="section">
    <div class="section-head" v-reveal>
      <span class="eyebrow">Testemunhas da Fé</span>
      <h2>Santos da Igreja Católica</h2>
      <p>
        Vidas que refletiram a luz de Cristo. Clique em um santo para conhecer
        sua história e seu testemunho.
      </p>
    </div>

    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="card-grid">
      <SaintCard v-for="saint in saints" :key="saint.id" :saint="saint" />
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import SaintCard from "../components/SaintCard.vue";

const saints = ref([]);
const loading = ref(true);
const error = ref("");

async function fetchSaints() {
  loading.value = true;
  error.value = "";
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/saints");
    saints.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar os santos.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchSaints);
</script>
