import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import BooksView from "../views/BooksView.vue";
import BookChaptersView from "../views/BookChaptersView.vue";
import ChapterView from "../views/ChapterView.vue";
import AngelsView from "../views/AngelsView.vue";
import AngelDetailView from "../views/AngelDetailView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", name: "home", component: HomeView },
    { path: "/livros", name: "books", component: BooksView },
    { path: "/livro/:id", name: "book-chapters", component: BookChaptersView },
    { path: "/capitulo/:id", name: "chapter", component: ChapterView },
    { path: "/anjos", name: "angels", component: AngelsView },
    { path: "/anjos/:id", name: "angel-detail", component: AngelDetailView },
  ],
});

export default router;
