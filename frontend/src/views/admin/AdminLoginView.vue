<template>
  <section class="admin-login">
    <div class="login-card" v-reveal>
      <span class="eyebrow">Acesso Restrito</span>
      <h1>Painel Administrativo</h1>
      <p class="login-description">
        Entre com suas credenciais para gerenciar os conteúdos.
      </p>

      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <label for="username">Usuário</label>
          <input id="username" v-model="username" type="text" required />
        </div>
        <div class="form-group">
          <label for="password">Senha</label>
          <input id="password" v-model="password" type="password" required />
        </div>
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

const router = useRouter();
const route = useRoute();

const username = ref("");
const password = ref("");
const loading = ref(false);
const error = ref("");

async function handleLogin() {
  loading.value = true;
  error.value = "";

  try {
    const response = await axios.post("http://127.0.0.1:8000/api/auth/login", {
      username: username.value,
      password: password.value,
    });
    localStorage.setItem("admin_token", response.data.access_token);
    const redirect = route.query.redirect || "/admin";
    router.push(redirect);
  } catch (err) {
    error.value = "Usuário ou senha inválidos.";
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
