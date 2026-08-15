<template>
  <header class="app-header">
    <router-link to="/" class="logo">Bíblia Católica</router-link>
  </header>
  <main>
    <router-view />
  </main>
</template>

<script setup></script>

<style>
body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  background-color: #fafafa;
}
.app-header {
  background-color: #3f51b5;
  color: white;
  padding: 1rem;
}
.app-header a {
  color: white;
  text-decoration: none;
  font-size: 1.5rem;
}
main {
  padding: 1rem;
}
</style>
