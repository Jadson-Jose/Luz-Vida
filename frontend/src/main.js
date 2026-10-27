import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { reveal } from "./directives/reveal";
import { inject } from "@vercel/analytics"; // <-- NOVO IMPORT
import "./assets/styles.css";

const app = createApp(App);
app.directive("reveal", reveal);

inject(); // <-- NOVA LINHA (Ativa o rastreamento)

app.use(router);
app.mount("#app");