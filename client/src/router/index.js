import { createRouter, createWebHistory } from "vue-router"
import axios from "axios"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/auth",
            name: "auth",
            component: () => import("@/views/AuthView/AuthView.vue"),
            redirect: { name: "login" },
            children: [
                {
                    path: "/auth/login",
                    name: "login",
                    component: () => import("@/views/AuthView/LoginView.vue")
                }
                // {
                //     path: "/auth/register",
                //     name: "register",
                //     component: () => import("@/views/AuthView/RegisterView.vue")
                // }
            ],
            beforeEnter: async (to, from, next) => {
                await axios
                    .get("/user/me")
                    .then(() => next({ name: "home" }))
                    .catch(() => next())
            }
        },
        {
            path: "/",
            name: "base",
            component: () => import("@/views/BaseView.vue"),
            children: [
                {
                    path: "/",
                    name: "home",
                    component: () => import("@/views/HomeView.vue")
                }
            ],
            beforeEnter: async (to, from, next) => {
                await axios
                    .get("/user/me")
                    .then(() => next())
                    .catch(() => next({ name: "auth" }))
            }
        },
        {
            path: "/:pathMatch(.*)*",
            name: "404",
            component: () => import("@/views/404View.vue")
        }
    ]
})

export default router
