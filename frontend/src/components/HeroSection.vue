<template>
  <section class="hero">
    <div class="hero-copy">
      <span class="eyebrow">Fé · Tradição · Palavra de Deus</span>
      <h1>A luz que atravessa<br /><em>dois mil anos</em> de fé.</h1>
      <p class="lead">
        Leia, estude e medite a Palavra de Deus com a tradução católica de
        referência. Uma experiência de leitura serena e profunda.
      </p>
      <div class="hero-actions">
        <router-link to="/livros" class="btn btn-primary"
          >Ler a Bíblia</router-link
        >
        <a href="#versiculo" class="btn btn-ghost">Versículo do Dia</a>
      </div>
    </div>

    <div class="rose-wrap" aria-hidden="true">
      <svg viewBox="0 0 600 600" id="roseSvg">
        <defs>
          <radialGradient id="gGold" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#F1DFA6" />
            <stop offset="100%" stop-color="#B8892B" />
          </radialGradient>
          <radialGradient id="gBlue" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#3A4E9C" />
            <stop offset="100%" stop-color="#101c46" />
          </radialGradient>
          <radialGradient id="gWine" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#A5384A" />
            <stop offset="100%" stop-color="#591420" />
          </radialGradient>
        </defs>
        <circle
          cx="300"
          cy="300"
          r="290"
          fill="none"
          stroke="#B8892B"
          stroke-width="1.5"
          opacity="0.5"
        />
        <circle
          cx="300"
          cy="300"
          r="260"
          fill="none"
          stroke="#B8892B"
          stroke-width="1"
          opacity="0.35"
        />
        <g id="roseGroup"></g>
        <circle
          cx="300"
          cy="300"
          r="46"
          fill="#F6EFDC"
          stroke="#B8892B"
          stroke-width="2.5"
        />
        <path
          d="M300 278V322M280 300H320"
          stroke="#7E1E2C"
          stroke-width="4"
          stroke-linecap="round"
        />
      </svg>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from "vue";

function generateRose() {
  const ns = "http://www.w3.org/2000/svg";
  const group = document.getElementById("roseGroup");
  if (!group) return;

  const cx = 300,
    cy = 300;
  const colors = ["url(#gGold)", "url(#gBlue)", "url(#gWine)"];
  const petals = 12;

  for (let i = 0; i < petals; i++) {
    const angle = (360 / petals) * i;
    const petal = document.createElementNS(ns, "path");
    petal.setAttribute(
      "d",
      "M300,300 C280,240 270,180 300,120 C330,180 320,240 300,300 Z",
    );
    petal.setAttribute("fill", colors[i % colors.length]);
    petal.setAttribute("stroke", "#F6EFDC");
    petal.setAttribute("stroke-width", "1.4");
    petal.setAttribute("opacity", "0.92");
    petal.setAttribute("transform", `rotate(${angle} ${cx} ${cy})`);
    group.appendChild(petal);
  }

  for (let i = 0; i < petals; i++) {
    const angle = (360 / petals) * i + 360 / petals / 2;
    const tip = document.createElementNS(ns, "circle");
    tip.setAttribute("cx", cx);
    tip.setAttribute("cy", 90);
    tip.setAttribute("r", 6);
    tip.setAttribute("fill", "#B8892B");
    tip.setAttribute("transform", `rotate(${angle} ${cx} ${cy})`);
    group.appendChild(tip);
  }
}

onMounted(generateRose);
</script>
