<script setup>
import BlockBorder from "@/components/BlockBorder.vue"
</script>

<template>
    <div class="auth">
        <div class="auth-container">
            <img alt="logo" class="auth-container-bg" src="@/assets/auth-bg.svg" />
            <BlockBorder class="auth-container-border" color="grey" radius="35">
                <RouterView />
            </BlockBorder>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.auth {
    @apply w-full h-screen flex items-center justify-center;

    &-container {
        @apply w-1/2 h-1/2 relative flex items-center justify-end rounded-xl overflow-hidden border border-dark-50;

        &-border {
            @apply w-1/2 h-full z-10 shadow-2xl transition-all duration-300;
        }

        &-bg {
            @apply w-full h-full absolute;
        }
    }
}
</style>
