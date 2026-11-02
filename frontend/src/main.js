import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { reveal } from "./directives/reveal";
import { inject } from "@vercel/analytics/vue";
import { createHead } from "@unhead/vue"; // <-- NOVO IMPORT
import "./assets/styles.css";

const app = createApp(App);
const head = createHead(); // <-- CRIA O GERENCIADOR

app.directive("reveal", reveal);
app.use(router);
app.use(head); // <-- INJETA NO APP
inject();

app.mount("#app");