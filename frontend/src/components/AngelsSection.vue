<template>
  <section id="anjos">
    <div class="section-head" v-reveal>
      <span class="eyebrow">Os Mensageiros Celestes</span>
      <h2>Anjos e Arcanjos</h2>
      <p>
        Espíritos criados para adorar a Deus e servir de ponte entre o Céu e a
        Terra. Conheça quem são e o papel de cada um na história da salvação.
      </p>
    </div>

    <div class="card-grid">
      <article
        v-for="angel in angels"
        :key="angel.title"
        class="card"
        :class="{ expanded: angel.expanded }"
        v-reveal
      >
        <div class="icon" v-html="icons[angel.icon]"></div>
        <span class="tag">{{ angel.tag }}</span>
        <h3>{{ angel.title }}</h3>
        <p>{{ angel.text }}</p>
        <div class="more">
          <p>{{ angel.more }}</p>
        </div>
        <button
          class="card-toggle"
          type="button"
          :aria-expanded="angel.expanded"
          @click="toggleAngel(angel)"
        >
          {{ angel.expanded ? "Ler menos " : "Leia mais " }}
          <svg viewBox="0 0 12 8" fill="none">
            <path
              d="M1 1L6 6L11 1"
              stroke="currentColor"
              stroke-width="1.6"
              stroke-linecap="round"
            />
          </svg>
        </button>
      </article>
    </div>
  </section>
</template>

<script setup>
import { reactive } from "vue";

// Ícones SVG (mesmos do template original)
const icons = {
  shield: `<svg viewBox="0 0 40 40" fill="none"><path d="M20 4L34 10V19C34 28 28 34 20 37C12 34 6 28 6 19V10L20 4Z" stroke="currentColor" stroke-width="1.6"/><path d="M14 20L18 24L27 14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>`,
  lily: `<svg viewBox="0 0 40 40" fill="none"><path d="M20 36V16" stroke="currentColor" stroke-width="1.6"/><path d="M20 16C20 8 12 8 10 4C10 12 14 16 20 16Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M20 16C20 8 28 8 30 4C30 12 26 16 20 16Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M20 16C20 10 20 6 20 3" stroke="currentColor" stroke-width="1.6"/></svg>`,
  fish: `<svg viewBox="0 0 40 40" fill="none"><path d="M4 20C12 10 28 10 36 20C28 30 12 30 4 20Z" stroke="currentColor" stroke-width="1.6"/><circle cx="14" cy="18" r="1.4" fill="currentColor"/><path d="M20 16V24" stroke="currentColor" stroke-width="1.2"/></svg>`,
  wing: `<svg viewBox="0 0 40 40" fill="none"><path d="M6 30C10 18 18 8 34 6C30 14 30 20 34 24C24 22 16 24 6 30Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M10 26C16 20 22 16 30 12" stroke="currentColor" stroke-width="1.2"/></svg>`,
  rings: `<svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="16" stroke="currentColor" stroke-width="1.4"/><circle cx="20" cy="20" r="10" stroke="currentColor" stroke-width="1.4"/><circle cx="20" cy="20" r="4" fill="currentColor"/></svg>`,
  flame: `<svg viewBox="0 0 40 40" fill="none"><path d="M20 4C22 10 28 14 28 22C28 29 24 34 20 34C16 34 12 29 12 22C12 20 13 18 14 17C14 22 17 24 18 22C15 16 18 8 20 4Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>`,
};

// Dados dos anjos (copiados do template)
const angels = reactive([
  {
    tag: "Príncipe da Milícia Celeste",
    title: "São Miguel Arcanjo",
    icon: "shield",
    text: 'Seu nome significa "Quem como Deus?" — o brado de fidelidade que ecoou contra a revolta de Lúcifer.',
    more: "É invocado como protetor da Igreja contra o mal, capitão dos exércitos celestiais e aquele que, segundo o Apocalipse, enfrenta o dragão. A tradição o venera como padroeiro dos que defendem a fé.",
    expanded: false,
  },
  {
    tag: "Mensageiro da Anunciação",
    title: "São Gabriel Arcanjo",
    icon: "lily",
    text: 'O anjo que trouxe a Maria o anúncio da encarnação do Verbo: "Ave, cheia de graça."',
    more: 'Antes já havia anunciado a Zacarias o nascimento de João Batista. Seu nome, "Força de Deus", marca-o como o mensageiro dos grandes anúncios da salvação.',
    expanded: false,
  },
  {
    tag: "Médico de Deus",
    title: "São Rafael Arcanjo",
    icon: "fish",
    text: 'Guiou o jovem Tobias e devolveu a visão a seu pai — seu nome significa "Deus cura".',
    more: 'É padroeiro dos viajantes, dos enfermos e dos médicos. No Livro de Tobias revela-se como "um dos sete que estão diante da glória do Senhor".',
    expanded: false,
  },
  {
    tag: "Companheiro de Cada Dia",
    title: "Anjo da Guarda",
    icon: "wing",
    text: "A cada pessoa foi confiado um anjo que a acompanha, protege e intercede desde o nascimento.",
    more: "A tradição da Igreja ensina que este anjo nos ilumina, guia e defende, sem nunca forçar a liberdade humana — um sussurro silencioso rumo ao bem.",
    expanded: false,
  },
  {
    tag: "A Hierarquia Celeste",
    title: "Os Nove Coros Angelicais",
    icon: "rings",
    text: "Serafins, Querubins, Tronos, Dominações, Virtudes, Potestades, Principados, Arcanjos e Anjos.",
    more: "Essa ordenação, sistematizada por Pseudo-Dionísio Areopagita, descreve diferentes graus de proximidade e serviço diante do trono de Deus, cada coro com uma missão própria na criação.",
    expanded: false,
  },
  {
    tag: "Presença nas Escrituras",
    title: "Anjos na Sagrada Escritura",
    icon: "flame",
    text: "Do Éden ao Apocalipse, os anjos anunciam, protegem, louvam e executam a vontade divina.",
    more: 'Aparecem a Abraão, lutam com Jacó, alimentam Elias, anunciam o nascimento e a ressurreição de Cristo, e cantam eternamente o "Santo, Santo, Santo" diante do trono.',
    expanded: false,
  },
]);

function toggleAngel(angel) {
  angel.expanded = !angel.expanded;
}
</script>
