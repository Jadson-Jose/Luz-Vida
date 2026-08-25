<template>
  <section class="chapter-reader">
    <div class="chapter-header">
      <router-link
        v-if="bookId"
        :to="{ name: 'book-chapters', params: { id: bookId } }"
        class="back-link"
      >
        ← Voltar aos capítulos
      </router-link>
      <h1>Capítulo {{ chapterNumber }}</h1>
    </div>

    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="verses">
      <p v-for="verse in verses" :key="verse.id" class="verse">
        <sup class="verse-number">{{ verse.number }}</sup> {{ verse.text }}
      </p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const verses = ref([]);
const chapterNumber = ref("");
const bookId = ref(null);
const loading = ref(true);
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
    bookId.value = response.data.book_id;
  } catch (err) {
    error.value = "Erro ao carregar o capítulo.";
    console.error(err);
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
.chapter-header {
  margin-bottom: 1.5rem;
}
.back-link {
  display: inline-block;
  margin-bottom: 1rem;
  color: var(--wine);
  font-family: "Cinzel", serif;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
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
  color: var(--wine);
}
</style>
