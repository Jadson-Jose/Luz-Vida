<template>
  <div>
    <HeroSection />

    <div v-if="lastReadChapter" class="continue-reading-container">
      <router-link :to="{ name: 'chapter', params: { id: lastReadChapter } }" class="btn-continue">
        📖 Voltar para onde parei
      </router-link>
    </div>

    <VerseCard />
    <BookGrid :books="books" :loading="loading" :error="error" />
    <AngelsSection />
    <HistorySection />
  </div>
  <PrayerBand />
</template>

<script setup>
import PrayerBand from "../components/PrayerBand.vue";
import HistorySection from "../components/HistorySection.vue";
import VerseCard from "../components/VerseCard.vue";
import AngelsSection from "../components/AngelsSection.vue";
import BookGrid from "../components/BookGrid.vue";
import HeroSection from "../components/HeroSection.vue";
import { ref, onMounted } from "vue";
import api from "../api/client";

const books = ref([]);
const loading = ref(false);
const error = ref("");

// Pega o ID do último capítulo lido do localStorage
const lastReadChapter = ref(localStorage.getItem('last_read_chapter'));

async function fetchBooks() {
  loading.value = true;
  error.value = "";
  try {
    const response = await api.get("books");
    books.value = response.data;
  } catch (err) {
    error.value = "Erro ao carregar os livros. Verifique se a API está rodando.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchBooks);
</script>

<style scoped>
.continue-reading-container {
  text-align: center;
  margin: -20px auto 40px auto;
  position: relative;
  z-index: 10;
}

.btn-continue {
  background: var(--blue-deep);
  color: var(--gold-pale);
  text-decoration: none;
  padding: 12px 24px;
  border-radius: 30px;
  font-family: 'Cinzel', serif;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  transition: transform 0.2s, background 0.2s;
  display: inline-block;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.btn-continue:hover {
  background: var(--wine);
  transform: translateY(-2px);
}
</style>