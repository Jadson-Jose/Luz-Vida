<template>
  <section class="chapter-reader" :class="{ 'dark-mode': isDarkMode }">
    <div class="reader-toolbar">
      <div class="nav-buttons top-nav">
        <router-link v-if="prevId" :to="{ name: 'chapter', params: { id: prevId } }" class="btn-nav">← Anterior</router-link>
        <span v-else class="btn-nav disabled">← Anterior</span>
        
        <router-link v-if="nextId" :to="{ name: 'chapter', params: { id: nextId } }" class="btn-nav">Próximo →</router-link>
        <span v-else class="btn-nav disabled">Próximo →</span>
      </div>

      <div class="settings-buttons">
        <button @click="decreaseFont" class="btn-icon" title="Diminuir Fonte">A-</button>
        <button @click="increaseFont" class="btn-icon" title="Aumentar Fonte">A+</button>
        <button @click="toggleDarkMode" class="btn-icon" title="Alternar Tema">
          {{ isDarkMode ? '☀️' : '🌙' }}
        </button>
      </div>
    </div>

    <div class="chapter-header">
      <router-link v-if="bookId" :to="{ name: 'book-chapters', params: { id: bookId } }" class="back-link">
        ← Voltar aos capítulos
      </router-link>
      <h1>{{ bookName }} {{ chapterNumber }}</h1>
    </div>

    <div v-if="loading" class="loading">Carregando…</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="verses" :style="{ fontSize: fontSize + 'rem' }">
      <p v-for="verse in verses" :key="verse.id" class="verse">
        <sup class="verse-number">{{ verse.number }}</sup> {{ verse.text }}
        
        <!-- Botão de compartilhar versículo -->
        <button class="share-btn" @click="shareVerse(verse)" title="Copiar versículo">🔗</button>
      </p>
    </div>

    <div class="nav-buttons bottom-nav">
      <router-link v-if="prevId" :to="{ name: 'chapter', params: { id: prevId } }" class="btn-nav">← Anterior</router-link>
      <router-link v-if="nextId" :to="{ name: 'chapter', params: { id: nextId } }" class="btn-nav">Próximo →</router-link>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import api from "../api/client";

const route = useRoute();
const verses = ref([]);
const chapterNumber = ref("");
const bookName = ref("");
const bookId = ref(null);
const loading = ref(true);
const error = ref("");

// Navegação
const prevId = ref(null);
const nextId = ref(null);

// Preferências do Leitor
const isDarkMode = ref(localStorage.getItem('reader-theme') === 'dark');
const fontSize = ref(parseFloat(localStorage.getItem('reader-font-size')) || 1.2);

const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value;
  localStorage.setItem('reader-theme', isDarkMode.value ? 'dark' : 'light');
};

const increaseFont = () => {
  if (fontSize.value < 2.0) {
    fontSize.value += 0.1;
    localStorage.setItem('reader-font-size', fontSize.value);
  }
};

const decreaseFont = () => {
  if (fontSize.value > 0.9) {
    fontSize.value -= 0.1;
    localStorage.setItem('reader-font-size', fontSize.value);
  }
};

async function fetchChapter() {
  loading.value = true;
  error.value = "";
  try {
    // Busca o capítulo e a navegação em paralelo
    const [chapterRes, navRes] = await Promise.all([
      api.get(`chapters/${route.params.id}`),
      api.get(`chapters/${route.params.id}/navigation`)
    ]);

    chapterNumber.value = navRes.data.chapter_number;
    bookName.value = navRes.data.book_name;
    prevId.value = navRes.data.prev_id;
    nextId.value = navRes.data.next_id;
    
    verses.value = chapterRes.data.verses;
    bookId.value = chapterRes.data.book_id;
  } catch (err) {
    error.value = "Erro ao carregar o capítulo.";
    console.error(err);
  } finally {
    loading.value = false;
  }
}

const shareVerse = (verse) => {
  const textToShare = `"${verse.text}" - ${bookName.value} ${chapterNumber.value}:${verse.number} (Luz-Vida)`;
  navigator.clipboard.writeText(textToShare);
  alert("Versículo copiado para a área de transferência!");
};

// Escuta mudanças de rota (para quando clicar em "Próximo")
watch(() => route.params.id, fetchChapter);

onMounted(fetchChapter);
</script>

<style scoped>
.chapter-reader {
  max-width: 700px;
  margin: 0 auto;
  padding: 1rem;
  transition: background-color 0.3s, color 0.3s;
  min-height: 100vh;
}

/* Tema Escuro */
.chapter-reader.dark-mode {
  background-color: #1a1a1a;
  color: #e0e0e0;
}
.chapter-reader.dark-mode h1,
.chapter-reader.dark-mode .verse {
  color: #e0e0e0;
}
.chapter-reader.dark-mode .back-link {
  color: #d4af37; 
}

/* Barra de Ferramentas */
.reader-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #ddd;
}
.dark-mode .reader-toolbar {
  border-bottom-color: #444;
}

.settings-buttons {
  display: flex;
  gap: 0.5rem;
}
.btn-icon {
  background: none;
  border: 1px solid #ccc;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  color: inherit;
}
.btn-icon:hover {
  background: #eee;
}
.dark-mode .btn-icon {
  border-color: #555;
}
.dark-mode .btn-icon:hover {
  background: #333;
}

/* Navegação */
.nav-buttons {
  display: flex;
  justify-content: space-between;
  margin: 2rem 0;
}
.btn-nav {
  text-decoration: none;
  color: var(--blue);
  font-family: 'Cinzel', serif;
  font-size: 0.85rem;
  text-transform: uppercase;
}
.dark-mode .btn-nav {
  color: #d4af37;
}
.btn-nav.disabled {
  color: #999;
  cursor: not-allowed;
}

/* Versículos */
.verses {
  transition: font-size 0.2s;
}
.verse {
  margin-bottom: 1rem;
  line-height: 1.8;
  position: relative;
}
.verse-number {
  font-weight: bold;
  margin-right: 0.25rem;
  color: var(--wine);
}
.dark-mode .verse-number {
  color: #d4af37;
}

/* Botão de Copiar (Aparece ao passar o mouse) */
.share-btn {
  background: none;
  border: none;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.2s;
  margin-left: 10px;
  font-size: 0.9rem;
}
.verse:hover .share-btn {
  opacity: 1;
}
</style>