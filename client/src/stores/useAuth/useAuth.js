import { defineStore } from "pinia"
import axios from "axios"
import { computed, ref } from "vue"
import router from "@/router/index.js"

export const useAuth = defineStore("auth", () => {
    const error = ref(false)

    const get_error = computed(() => {
        return error.value
    })

    const loging = async (login, password) => {
        await axios
            .post("/user/login", {
                name: login,
                password: password
            })
            .then(() => {
                error.value = false
                router.push({ name: "home" })
            })
            .catch(() => {
                error.value = true
            })
    }

    return {
        loging,
        get_error
    }
})
