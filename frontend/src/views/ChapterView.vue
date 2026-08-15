<template>
  <div class="chapter-reader">
    <h1>Capítulo {{ chapterNumber }}</h1>
    <p v-if="loading">Carregando...</p>
    <p v-if="error" class="error">{{ error }}</p>
    <div v-if="verses.length" class="verses">
      <p v-for="verse in verses" :key="verse.id" class="verse">
        <sup class="verse-number">{{ verse.number }}</sup> {{ verse.text }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const verses = ref([]);
const chapterNumber = ref("");
const loading = ref(false);
const error = ref("");

async function fetchChapter() {
  loading.value = true;
  error.value = "";
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/chapters/${route.params.id}`,
    );
    chapterNumber.value = response.data.number;
    verses.value = response.data.verses;
  } catch (err) {
    error.value = "Erro ao carregar o capítulo.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchChapter);
</script>

<style scoped>
.chapter-reader {
  max-width: 700px;
  margin: 0 auto;
  padding: 1rem;
}
.verse {
  margin-bottom: 0.75rem;
  line-height: 1.5;
}
.verse-number {
  font-weight: bold;
  margin-right: 0.25rem;
}
.error {
  color: red;
}
</style>
