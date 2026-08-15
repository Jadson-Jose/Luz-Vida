<template>
  <section id="versiculo" class="verse-section">
    <div v-reveal class="verse-card">
      <span class="eyebrow">Versículo do Dia</span>
      <p class="verse-text">{{ verse.text }}</p>
      <p class="verse-ref">{{ verse.ref }}</p>
      <button class="verse-refresh" @click="refreshVerse">
        Outra Palavra ✦
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";

const verses = [
  { text: "Tudo posso Naquele que me fortalece.", ref: "Filipenses 4,13" },
  { text: "O Senhor é o meu pastor; nada me faltará.", ref: "Salmo 23,1" },
  { text: "Porque para Deus nada é impossível.", ref: "Lucas 1,37" },
  { text: "Permanecei em mim, e eu permanecerei em vós.", ref: "João 15,4" },
  { text: "Não temas, porque eu sou contigo.", ref: "Isaías 41,10" },
  {
    text: "A fé é a certeza das coisas que se esperam, a convicção das coisas que se não veem.",
    ref: "Hebreus 11,1",
  },
  { text: "Amai-vos uns aos outros, como eu vos amei.", ref: "João 13,34" },
  {
    text: "Vinde a mim, todos os que estais cansados e sobrecarregados, e eu vos aliviarei.",
    ref: "Mateus 11,28",
  },
  {
    text: "O amor é paciente, é bondoso; o amor não é invejoso.",
    ref: "1 Coríntios 13,4",
  },
  {
    text: "Entregai ao Senhor o vosso caminho, confiai nele, e ele agirá.",
    ref: "Salmo 37,5",
  },
  {
    text: "Bem-aventurados os puros de coração, porque eles verão a Deus.",
    ref: "Mateus 5,8",
  },
  {
    text: "Eis que estou convosco todos os dias, até a consumação dos séculos.",
    ref: "Mateus 28,20",
  },
];

const verse = ref(verses[Math.floor(Math.random() * verses.length)]);

function refreshVerse() {
  let next;
  do {
    next = Math.floor(Math.random() * verses.length);
  } while (verses[next] === verse.value && verses.length > 1);
  verse.value = verses[next];
}
</script>
