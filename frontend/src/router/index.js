import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import BooksView from "../views/BooksView.vue";
import BookChaptersView from "../views/BookChaptersView.vue";
import ChapterView from "../views/ChapterView.vue";
import AngelsView from "../views/AngelsView.vue";
import AngelDetailView from "../views/AngelDetailView.vue";
import AdminLoginView from "../views/admin/AdminLoginView.vue";
import AdminLayout from "../views/admin/AdminLayout.vue";
import AdminDashboardView from "../views/admin/AdminDashboardView.vue";
import SaintsView from "../views/SaintsView.vue";
import SaintDetailView from "../views/SaintDetailView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", name: "home", component: HomeView },
    { path: "/livros", name: "books", component: BooksView },
    { path: "/livro/:id", name: "book-chapters", component: BookChaptersView },
    { path: "/capitulo/:id", name: "chapter", component: ChapterView },
    { path: "/anjos", name: "angels", component: AngelsView },
    { path: "/anjos/:id", name: "angel-detail", component: AngelDetailView },
    { path: "/admin/login", name: "admin-login", component: AdminLoginView },
    { path: "/santos", name: "saints", component: SaintsView },
    { path: "/santos/:id", name: "saint-detail", component: SaintDetailView },
    {
      path: "/admin",
      component: AdminLayout,
      meta: { requiresAuth: true },
      children: [
        {
          path: "",
          name: "admin-dashboard",
          component: { template: "<h1>Dashboard Admin</h1>" },
        },
        {
          path: "livros",
          name: "admin-books",
          component: () => import("../views/admin/AdminBooksView.vue"),
        },
        {
          path: "livros/:bookId/capitulos",
          name: "admin-chapters",
          component: () => import("../views/admin/AdminChaptersView.vue"),
        },
        {
          path: "capitulos/:chapterId/versiculos",
          name: "admin-verses",
          component: () => import("../views/admin/AdminVersesView.vue"),
        },
        {
          path: "anjos",
          name: "admin-angels",
          component: () => import("../views/admin/AdminAngelsView.vue"),
        },
        {
          path: "",
          name: "admin-dashboard",
          component: AdminDashboardView,
        },
        {
          path: "santos",
          name: "admin-saints",
          component: () => import("../views/admin/AdminSaintsView.vue"),
        },
      ],
    },
  ],
});

// Guard global de autenticação
router.beforeEach((to, from) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  const token = localStorage.getItem("admin_token");

  if (requiresAuth && !token) {
    return { name: "admin-login", query: { redirect: to.fullPath } };
  }
  // Retornar true ou undefined é permitido
  return true;
});

export default router;
