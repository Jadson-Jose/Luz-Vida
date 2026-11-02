import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { reveal } from "./directives/reveal";
import { inject } from "@vercel/analytics/vue";
import { createHead } from "@unhead/vue/client"; // <-- CORREÇÃO AQUI (adicione o /client)
import "./assets/styles.css";

const app = createApp(App);
const head = createHead(); 

app.directive("reveal", reveal);
app.use(router);
app.use(head); 
inject();

app.mount("#app");