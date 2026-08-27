<template>
  <header>
    <div class="nav-wrap">
      <router-link to="/" class="brand">
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
          placeholder="Buscar na Bíblia…"
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
        <router-link to="/santos">Santos</router-link>
        <router-link to="/admin/login">Admin</router-link>
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
  console.log("Busca submetida:", q);
  if (q) {
    router.push({ name: "search", query: { q } });
  } else {
    router.push({ name: "search" });
  }
}
</script>

<style scoped>
header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(246, 239, 220, 0.92);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--parchment-line);
}

.nav-wrap {
  max-width: 1180px;
  margin: 0 auto;
  padding: 14px 28px;
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
}

.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: "Cinzel", serif;
  font-size: 1.18rem;
  letter-spacing: 0.06em;
  color: var(--blue-deep);
  text-decoration: none;
  white-space: nowrap;
}

.brand svg {
  width: 32px;
  height: 32px;
}

.search-form {
  flex: 1 1 260px;
  display: flex;
  align-items: center;
  background: var(--parchment-deep);
  border: 1px solid var(--parchment-line);
  border-radius: 999px;
  padding: 8px 8px 8px 18px;
  min-width: 220px;
  transition:
    border-color 0.2s,
    box-shadow 0.2s;
}

.search-form:focus-within {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(184, 137, 43, 0.18);
}

.search-form input {
  flex: 1;
  border: none;
  background: transparent;
  font-family: "EB Garamond", serif;
  font-size: 1rem;
  color: var(--ink);
  outline: none;
}

.search-form input::placeholder {
  color: var(--ink-soft);
  font-style: italic;
}

.search-form button {
  border: none;
  background: var(--blue-deep);
  color: var(--gold-pale);
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex: none;
  transition:
    background 0.2s,
    transform 0.2s;
}

.search-form button:hover {
  background: var(--wine);
  transform: scale(1.05);
}

.search-form button svg {
  width: 17px;
  height: 17px;
}

nav.links {
  display: flex;
  gap: 22px;
  align-items: center;
}

nav.links a {
  font-family: "Cinzel", serif;
  font-size: 0.78rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--ink-soft);
  padding-bottom: 3px;
  border-bottom: 1px solid transparent;
  transition:
    color 0.2s,
    border-color 0.2s;
}

nav.links a:hover,
nav.links a:focus-visible {
  color: var(--wine);
  border-color: var(--wine);
}

a:focus-visible,
button:focus-visible,
input:focus-visible {
  outline: 3px solid var(--gold);
  outline-offset: 2px;
}

@media (max-width: 880px) {
  .nav-wrap {
    flex-direction: column;
    align-items: stretch;
  }
  .search-form {
    min-width: 100%;
  }
  nav.links {
    justify-content: center;
    flex-wrap: wrap;
  }
}
</style>
