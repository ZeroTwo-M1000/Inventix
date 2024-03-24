import { createApp } from "vue"
import { createPinia } from "pinia"
import "boxicons/css/boxicons.min.css"
import "@/style.css"

import App from "./App.vue"
import router from "./router"
import axios from "axios"

export const BASE_URL = "http://localhost:8000"

axios.defaults.baseURL = `${BASE_URL}/api`
axios.defaults.withCredentials = true

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount("#app")
