<template>
  <div class="admin-layout">
    <aside class="admin-sidebar">
      <h2>Admin</h2>
      <nav>
        <router-link to="/admin">Dashboard</router-link>
        <router-link to="/admin/livros">Livros</router-link>
        <router-link to="/admin/anjos">Anjos</router-link>
        <router-link to="/admin/santos">Santos</router-link>
        <button @click="logout">Sair</button>
      </nav>
    </aside>
    <main class="admin-content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function logout() {
  localStorage.removeItem("admin_token");
  router.push("/admin/login");
}
</script>

<style scoped>
.admin-layout {
  display: flex;
  min-height: 100vh;
}

.admin-sidebar {
  width: 220px;
  background: var(--blue-deep);
  color: var(--gold-pale);
  padding: 1.5rem 1rem;
}

.admin-sidebar h2 {
  color: var(--gold-light);
  margin-bottom: 2rem;
  text-align: center;
}

.admin-sidebar nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.admin-sidebar a,
.admin-sidebar button {
  color: var(--gold-pale);
  text-decoration: none;
  background: none;
  border: none;
  padding: 0.6rem 1rem;
  text-align: left;
  font-family: "Cinzel", serif;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  cursor: pointer;
  border-radius: 4px;
  transition: background 0.2s;
}

.admin-sidebar a:hover,
.admin-sidebar button:hover {
  background: rgba(255, 255, 255, 0.1);
}

.admin-content {
  flex: 1;
  padding: 2rem;
  background: var(--parchment);
}
</style>
