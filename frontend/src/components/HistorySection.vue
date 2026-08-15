<template>
  <section id="historia">
    <div class="section-head" v-reveal>
      <span class="eyebrow">Dois Mil Anos de Fé</span>
      <h2>A História da Igreja</h2>
      <p>
        Do Cenáculo de Jerusalém aos dias de hoje: uma linha do tempo com os
        marcos que formaram a Igreja Católica.
      </p>
    </div>

    <div class="timeline">
      <div
        v-for="item in historyItems"
        :key="item.title"
        class="tl-item"
        v-reveal
      >
        <div class="tl-date">{{ item.date }}</div>
        <div class="tl-rail">
          <div class="tl-dot"></div>
          <div class="tl-line"></div>
        </div>
        <div class="tl-content">
          <div
            class="icon"
            style="
              color: var(--blue);
              width: 30px;
              height: 30px;
              margin-bottom: 8px;
            "
            v-html="icons[item.icon]"
          ></div>
          <h3>{{ item.title }}</h3>
          <p>{{ item.text }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { reactive } from "vue";

// Ícones SVG (mesmos usados no template original)
const icons = {
  dove: `<svg viewBox="0 0 40 40" fill="none"><path d="M6 22C12 16 20 16 24 22C28 18 34 18 36 14C34 22 28 26 22 26C16 26 10 26 6 22Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="26" cy="18" r="1.3" fill="currentColor"/></svg>`,
  flame: `<svg viewBox="0 0 40 40" fill="none"><path d="M20 4C22 10 28 14 28 22C28 29 24 34 20 34C16 34 12 29 12 22C12 20 13 18 14 17C14 22 17 24 18 22C15 16 18 8 20 4Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>`,
  scroll: `<svg viewBox="0 0 40 40" fill="none"><path d="M8 8C8 6 10 4 12 4H30V32C30 34 28 36 26 36H12C10 36 8 34 8 32V8Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M14 14H24M14 20H24M14 26H20" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>`,
  tower: `<svg viewBox="0 0 40 40" fill="none"><path d="M12 36V16L20 6L28 16V36" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M16 36V26H24V36" stroke="currentColor" stroke-width="1.4"/><path d="M20 6V2" stroke="currentColor" stroke-width="1.4"/></svg>`,
  book: `<svg viewBox="0 0 40 40" fill="none"><path d="M20 10C16 7 10 7 6 8V30C10 29 16 29 20 32C24 29 30 29 34 30V8C30 7 24 7 20 10Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M20 10V32" stroke="currentColor" stroke-width="1.4"/></svg>`,
  keys: `<svg viewBox="0 0 40 40" fill="none"><circle cx="12" cy="12" r="6" stroke="currentColor" stroke-width="1.6"/><path d="M16 16L32 32M25 25L29 21M28 28L32 24" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>`,
};

// Dados da linha do tempo
const historyItems = reactive([
  {
    date: "33 d.C.",
    icon: "dove",
    title: "Pentecostes — o Nascimento da Igreja",
    text: "O Espírito Santo desce sobre os Apóstolos reunidos com Maria no Cenáculo. Pedro prega e cerca de três mil pessoas se convertem: a Igreja começa sua missão ao mundo.",
  },
  {
    date: "Séc. I–IV",
    icon: "flame",
    title: "A Era dos Mártires",
    text: 'Sob perseguições romanas, cristãos como Estêvão, Inácio de Antioquia e Perpétua e Felicidade selam a fé com o sangue. "O sangue dos mártires é semente de novos cristãos."',
  },
  {
    date: "325",
    icon: "scroll",
    title: "Concílio de Niceia",
    text: "Reunidos por convocação imperial, os bispos definem o Credo niceno e afirmam a divindade de Cristo contra o arianismo — o primeiro grande concílio ecumênico.",
  },
  {
    date: "Séc. V–XV",
    icon: "tower",
    title: "Idade Média — Mosteiros e Catedrais",
    text: "Monges beneditinos preservam o saber, universidades nascem sob a Igreja, e catedrais góticas erguem-se como Bíblias em pedra e vitral, elevando o olhar ao Céu.",
  },
  {
    date: "1545–1563",
    icon: "book",
    title: "Concílio de Trento",
    text: "Diante da Reforma Protestante, a Igreja reafirma a doutrina católica, reorganiza a formação do clero e impulsiona a Reforma Católica com clareza doutrinal e disciplina pastoral.",
  },
  {
    date: "1962–1965",
    icon: "keys",
    title: "Concílio Vaticano II",
    text: "Convocado por João XXIII, renova a linguagem pastoral da Igreja, valoriza a liturgia em língua vernácula e o diálogo com o mundo contemporâneo, sem abandonar a Tradição.",
  },
]);
</script>
