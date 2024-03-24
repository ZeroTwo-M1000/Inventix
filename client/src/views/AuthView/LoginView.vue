<script setup>
import BlockBorder from "@/components/BlockBorder.vue"
import { useAuth } from "@/stores/useAuth/useAuth.js"
import { toRefs } from "vue"
import { ref } from "vue"

const auth = useAuth()
const { get_error } = toRefs(auth)

const login = ref("string")
const password = ref("string")
</script>

<template>
    <div class="auth-container-content">
        <div class="auth-container-content-title">
            <h1>Авторизация</h1>
        </div>
        <div class="auth-container-content-body">
            <BlockBorder class="input-border" color="grey" radius="15">
                <i class="bx bx-user"></i>
                <input v-model="login" placeholder="Логин" type="text" />
            </BlockBorder>
            <BlockBorder class="input-border" color="grey" radius="15">
                <i class="bx bx-lock-alt"></i>
                <input v-model="password" placeholder="Пароль" type="password" />
            </BlockBorder>
            <div v-show="get_error" class="error">
                <i class="bx bx-block"></i>
                <p>Неверный логин или пароль</p>
            </div>
        </div>
        <div class="auth-container-content-btn">
            <button @click="auth.loging(login, password)">Войти в аккаунт</button>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.auth-container-content {
    @apply w-full z-10 h-full flex flex-col items-center justify-evenly bg-dark-500 rounded-xl;

    &-title {
        @apply text-3xl transition-all duration-300 font-medium text-white;

        @screen 2xl {
            @apply text-4xl;
        }

        h1 {
            @apply select-none transition-all duration-300;
        }
    }

    &-body {
        @apply w-4/6 transition-all duration-300 relative;

        @screen 2xl {
            @apply text-lg;
        }

        .error {
            @apply w-full justify-center text-red flex items-center gap-3 mt-4;

            i {
                @apply text-xl;
            }
        }

        .input-border {
            @apply mt-4 flex items-center;

            i {
                @apply text-xl absolute text-dark-icon left-3;
            }
        }

        input {
            @apply w-full py-2 px-10 rounded-md outline-none bg-dark-300 border-2 border-transparent transition-all duration-300;

            &:focus {
                @apply border-2 border-blue;
            }
        }
    }

    &-btn {
        @apply w-1/2 transition-all duration-300;

        button {
            @apply w-full py-3 px-5 rounded-md outline-none bg-dark-300 hover:bg-blue transition-all duration-300;
        }
    }
}
</style>
