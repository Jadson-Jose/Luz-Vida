<template>
  <section class="admin-login">
    <div class="login-card" v-reveal>
      <span class="eyebrow">Acesso Restrito</span>
      <h1>Painel Administrativo</h1>
      <p class="login-description">
        Digite o token de acesso para gerenciar os conteúdos da Bíblia e dos
        Anjos.
      </p>

      <form @submit.prevent="handleLogin" class="login-form">
        <label for="token">Token de Acesso</label>
        <input
          id="token"
          v-model="token"
          type="password"
          placeholder="Digite o token"
          autocomplete="current-password"
          required
        />
        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? "Verificando…" : "Entrar" }}
        </button>
      </form>

      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import axios from "axios";
import api from "../../api/client";

const router = useRouter();
const route = useRoute();

const token = ref("");
const loading = ref(false);
const error = ref("");

async function handleLogin() {
  await api.get("/angels");
  loading.value = true;
  error.value = "";

  try {
    // Testa o token chamando uma rota protegida qualquer (ex.: listar anjos)
    await axios.get("http://127.0.0.1:8000/api/angels", {
      headers: { Authorization: `Bearer ${token.value}` },
    });

    // Se chegou aqui, o token é válido
    localStorage.setItem("admin_token", token.value);

    // Redireciona para a página que o usuário tentou acessar ou para o dashboard
    const redirect = route.query.redirect || "/admin";
    router.push(redirect);
  } catch (err) {
    error.value = "Token inválido. Verifique e tente novamente.";
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.admin-login {
  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.login-card {
  max-width: 420px;
  width: 100%;
  background: var(--parchment-deep);
  border: 1px solid var(--parchment-line);
  border-radius: 6px;
  padding: 3rem 2rem;
  text-align: center;
  box-shadow: var(--shadow);
}

.login-card h1 {
  margin: 0.5rem 0 1rem;
  font-size: 2rem;
}

.login-description {
  color: var(--ink-soft);
  margin-bottom: 2rem;
  font-size: 1rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  text-align: left;
}

.login-form label {
  font-family: "Cinzel", serif;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--blue-deep);
}

.login-form input {
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border: 1px solid var(--parchment-line);
  border-radius: 4px;
  background: var(--parchment);
  color: var(--ink);
}

.login-form input:focus {
  outline: none;
  border-color: var(--gold);
  box-shadow: 0 0 0 2px rgba(184, 137, 43, 0.2);
}

.error-message {
  color: var(--wine);
  margin-top: 1rem;
  font-style: italic;
}
</style>
