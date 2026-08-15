<template>
  <footer>
    <div class="footer-inner">
      <div>
        <div class="footer-brand">
          <svg viewBox="0 0 40 40" fill="none">
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
          </svg>
          Ecclesia
        </div>
        <p
          style="
            max-width: 34ch;
            color: var(--ink-soft);
            margin-top: 16px;
            font-size: 0.95rem;
          "
        >
          Um espaço de fé, memória e beleza para quem busca conhecer melhor a
          Palavra de Deus.
        </p>
      </div>
      <div class="footer-cols">
        <div class="footer-col">
          <span class="eyebrow">Navegar</span>
          <router-link to="/">Início</router-link>
          <router-link to="/livros">Livros</router-link>
        </div>
        <div class="footer-col">
          <span class="eyebrow">Comunidade</span>
          <a href="#versiculo">Versículo</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Ecclesia — feito com fé.</span>
      <span>"Tudo posso Naquele que me fortalece." — Fl 4,13</span>
    </div>
  </footer>
</template>
