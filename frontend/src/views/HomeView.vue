<template>
  <div>
    <HeroSection />

    <div v-if="lastReadChapter" class="continue-reading-container">
      <router-link :to="{ name: 'chapter', params: { id: lastReadChapter } }" class="btn-continue">
        📖 Voltar para onde parei
      </router-link>
    </div>

    <VerseCard />

    <!-- Seção de destaque para a Bíblia, mas SEM a grade pesada -->
    <section class="section home-bible-cta">
      <div class="section-head" v-reveal>
        <span class="eyebrow">Palavra de Deus</span>
        <h2>Explore a Bíblia Sagrada</h2>
        <p>Navegue por todos os livros, capítulos e versículos da Bíblia Católica.</p>
      </div>
      <div style="text-align: center; margin-top: 2rem;">
        <router-link to="/livros" class="btn btn-primary">Acessar todos os Livros</router-link>
      </div>
    </section>

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
import HeroSection from "../components/HeroSection.vue";
import { ref } from "vue";

// Pega o ID do último capítulo lido do localStorage
const lastReadChapter = ref(localStorage.getItem('last_read_chapter'));
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

.home-bible-cta {
  text-align: center;
}
</style>