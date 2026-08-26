<template>
  <router-link
    :to="{ name: 'saint-detail', params: { id: saint.id } }"
    class="card saint-card"
    v-reveal
  >
    <div class="saint-image">
      <img
        v-if="saint.image_url"
        :src="saint.image_url"
        :alt="saint.name"
        loading="lazy"
        @error="handleImageError"
      />
      <div v-else class="placeholder">✠</div>
    </div>
    <span class="tag">{{ saint.title || "Santo" }}</span>
    <h3>{{ saint.name }}</h3>
    <p>{{ saint.short_text }}</p>
    <span class="card-link">Ler mais →</span>
  </router-link>
</template>

<script setup>
defineProps({
  saint: {
    type: Object,
    required: true,
  },
});
function handleImageError(event) {
  console.error("Erro ao carregar imagem:", event.target.src);
  // Opcional: substitui por placeholder local
  event.target.style.display = "none";
}
</script>

<style scoped>
.saint-card {
  text-decoration: none;
  color: var(--ink);
  display: block;
  transition:
    transform 0.2s,
    box-shadow 0.2s,
    border-color 0.2s;
  height: 100%;
}
.saint-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow);
  border-color: var(--gold);
}
.saint-image {
  width: 100%;
  height: 180px;
  overflow: hidden;
  border-radius: 4px;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--parchment-line);
}
.saint-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.placeholder {
  font-size: 3rem;
  color: var(--wine);
}
.card-link {
  display: inline-block;
  margin-top: 16px;
  font-family: "Cinzel", serif;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--wine);
}
</style>
