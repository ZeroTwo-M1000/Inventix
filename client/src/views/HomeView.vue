<script setup>
import axios from "axios"
import { ref } from "vue"

const auth = ref()

async function get() {
    await axios.get("/user/me").then((res) => {
        auth.value = res.data
    })
}
</script>

<template>
    <h1 @click="get">Home</h1>
    <h1>{{ auth }}</h1>
</template>

<style lang="scss" scoped></style>
