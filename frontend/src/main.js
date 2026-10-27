import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { reveal } from "./directives/reveal";
import { inject } from "@vercel/analytics/vue"; // <-- AQUI ESTÁ A MUDANÇA
import "./assets/styles.css";

const app = createApp(App);
app.directive("reveal", reveal);

inject(); // Ativa o rastreamento integrado ao Vue Router

app.use(router);
app.mount("#app");