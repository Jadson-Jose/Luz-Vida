<template>
  <div class="pagination-bar">
    <button
      class="btn-page"
      :disabled="currentPage <= 1"
      @click="$emit('change-page', currentPage - 1)"
    >
      ← Anterior
    </button>
    <span class="page-info">
      Página {{ currentPage }} de {{ totalPages }}
    </span>
    <button
      class="btn-page"
      :disabled="currentPage >= totalPages"
      @click="$emit('change-page', currentPage + 1)"
    >
      Próxima →
    </button>
  </div>
</template>

<script setup>
defineProps({
  currentPage: { type: Number, required: true },
  totalPages: { type: Number, required: true },
});
defineEmits(["change-page"]);
</script>

<style scoped>
.pagination-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin: 1rem 0;
}
.btn-page {
  background: var(--parchment-deep);
  border: 1px solid var(--parchment-line);
  border-radius: 4px;
  padding: 0.4rem 0.8rem;
  cursor: pointer;
  font-family: "Cinzel", serif;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.btn-page:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.page-info {
  font-family: "Cinzel", serif;
  font-size: 0.8rem;
  color: var(--ink-soft);
}
</style>
