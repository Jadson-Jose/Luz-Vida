<template>
  <header>
    <div class="nav-wrap">
      <router-link to="/" class="brand">
        <!-- Mantenha o SVG do logo -->
        <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle
            cx="20"
            cy="20"
            r="18"
            stroke="var(--gold)"
            stroke-width="1.4"
          />
          <path
            d="M20 8V32M12 15H28"
            stroke="var(--wine)"
            stroke-width="2"
            stroke-linecap="round"
          />
          <path d="M20 8L22 12H18L20 8Z" fill="var(--gold)" />
        </svg>
        Ecclesia
      </router-link>

      <form class="search-form" @submit.prevent="handleSearch">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Buscar livros, capítulos…"
          aria-label="Buscar"
        />
        <button type="submit" aria-label="Pesquisar">
          <svg viewBox="0 0 24 24" fill="none">
            <circle
              cx="11"
              cy="11"
              r="7"
              stroke="currentColor"
              stroke-width="2"
            />
            <path
              d="M21 21L16.65 16.65"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
            />
          </svg>
        </button>
      </form>

      <nav class="links">
        <router-link to="/">Início</router-link>
        <router-link to="/livros">Livros</router-link>
        <router-link to="/anjos">Anjos</router-link>
        <a href="#sobre">Sobre</a>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const searchQuery = ref("");

function handleSearch() {
  const q = searchQuery.value.trim();
  if (q) {
    router.push({ name: "books", query: { search: q } });
  } else {
    router.push({ name: "books" });
  }
}
</script>
