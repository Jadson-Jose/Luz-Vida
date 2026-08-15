<template>
  <div>
    <HeroSection />
    <VerseCard />
    <!-- <BookGrid :books="books" :loading="loading" :error="error" /> -->
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
import HeroSection from "../components/HeroSection.vue"; // ← adicionar
import { ref, onMounted } from "vue";
import axios from "axios";

const books = ref([]);
const loading = ref(false);
const error = ref("");

async function fetchBooks() {
  loading.value = true;
  error.value = "";
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/books");
    books.value = response.data;
  } catch (err) {
    error.value =
      "Erro ao carregar os livros. Verifique se a API está rodando.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchBooks);
</script>
